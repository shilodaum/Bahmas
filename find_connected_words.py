from itertools import product
from pathlib import Path

import numpy as np
from nltk.stem.porter import PorterStemmer

import matplotlib.pyplot as plt


class Searcher:
    def __init__(self, file_path: Path):
        self.content = file_path.read_text()

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


THRESHOLD = 5

if __name__ == '__main__':
    # optional_words = ["hello", "boo", "girls", "goo", "moo"]
    directory_name = "../foo"
    #
    # scanner = DirectoryScanner(directory_name, StemSearcher)
    #
    # popular_words = {word: scanner.count_files_with_keywords([word]) for word in optional_words}
    # popular_words = {word: count for word, count in popular_words.items() if count >= THRESHOLD}

    words = Path("one_route.txt").read_text().split()
    popular_words = set(words)
    popular_words = {word: words.count(word) for word in popular_words}
    popular_words = {word: count for word, count in popular_words.items() if count >= THRESHOLD}
    scanner = DirectoryScanner(directory_name, RawSearcher)

    print("calculating occurrences")
    joint_occurrences = [
        [2 * scanner.count_files_with_keywords((word1, word2)) / (popular_words[word1] + popular_words[word2]) for word1
         in popular_words] for word2 in
        reversed(popular_words)]
    print("done occurrences")

    reversed_words = [word[::-1] for word in popular_words]
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(len(reversed_words)), labels=reversed_words, rotation=45)
    ax.set_yticks(np.arange(len(reversed_words)), labels=list(reversed(reversed_words)))

    # for i in range(len(popular_words)):
    #     for j in range(len(popular_words)):
    #         ax.text(j, i, round(joint_occurrences[i][j], 2),
    #                 ha="center", va="center", color="g")
    plt.imshow(joint_occurrences, cmap='hot', interpolation='nearest')
    plt.show()
