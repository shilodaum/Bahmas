import pickle
from itertools import product
from pathlib import Path

import numpy as np
from nltk.stem.porter import PorterStemmer

import matplotlib.pyplot as plt


class Searcher:
    def __init__(self, file_path: Path):
        self.content = file_path.read_text().split()

    def search_multiple_keywords_in_file(self, keywords):
        for keyword in keywords:
            if not self._search(keyword):
                return False
        return True


class RawSearcher(Searcher):
    def _search(self, word):
        return word in self.content


class StemSearcher(Searcher):
    def __init__(self, file_path: Path):
        super().__init__(file_path)
        self.content = self.content.split()

        stemmer = PorterStemmer()
        self.content = [stemmer.stem(word) for word in self.content]

    def _search(self, word):
        # print(PorterStemmer().stem(word))
        return PorterStemmer().stem(word) in self.content


class DirectoryScanner:
    def __init__(self, directory_name, searcher_type):
        self.directory_path = Path(directory_name)
        self.searcher_type = searcher_type

    def count_files_with_keywords(self, keywords):
        count = 0
        for filename in self.directory_path.iterdir():
            count += self.searcher_type(filename).search_multiple_keywords_in_file(keywords)

        return count


def jaccard_similarity(word1, word2, scanner, words_occurrences_in_files):
    intersection = scanner.count_files_with_keywords((word1, word2))
    union = words_occurrences_in_files[word1] + words_occurrences_in_files[word2] - intersection
    return intersection / union



THRESHOLD = 500


def calc_popular_words(popular_words_file):
    words = Path(popular_words_file).read_text().split()
    popular_words = set(words)
    popular_words = {word: words.count(word) for word in popular_words}
    popular_words = {word: count for word, count in popular_words.items() if count >= THRESHOLD}

    with open("popular_words.pkl", 'wb') as f:
        pickle.dump(popular_words, f)


def calc_joint_occurrences(directory_name, popular_words):
    scanner = DirectoryScanner(directory_name, RawSearcher)

    words_occurrences_in_files = {word: scanner.count_files_with_keywords([word]) for word in popular_words}

    joint_occurrences = [
        [jaccard_similarity(word1, word2, scanner, words_occurrences_in_files) for word1 in popular_words] for word2 in
        reversed(popular_words)]

    with open("joint_occurrences.pkl", 'wb') as f:
        pickle.dump(joint_occurrences, f)


def plot_joint_occurrences(popular_words):
    reversed_words = [word[::-1] for word in popular_words]
    with open("joint_occurrences.pkl", 'rb') as f:
        joint_occurrences = pickle.load(f)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xticks(np.arange(len(reversed_words)), labels=reversed_words, rotation=45)
    ax.set_yticks(np.arange(len(reversed_words)), labels=list(reversed(reversed_words)))

    plt.rc('font', size=8)

    for i in range(len(popular_words)):
        for j in range(len(popular_words)):
            ax.text(j, i, round(joint_occurrences[i][j], 2),
                    ha="center", va="center", color="g")
    plt.imshow(joint_occurrences, cmap='GnBu', interpolation='nearest')
    plt.show()


if __name__ == '__main__':
    directory_name = "titles"

    # calc_popular_words("demo_text.txt")
    with open("popular_words.pkl", 'rb') as f:
        popular_words = pickle.load(f)
    # calc_joint_occurrences(directory_name, popular_words)
    plot_joint_occurrences(popular_words)
