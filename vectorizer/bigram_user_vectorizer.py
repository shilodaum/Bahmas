from collections import Counter
from functools import partial

from super_vector import SuperVector
from vectorizer.utils import get_features, in_sorted_list, BI_PREFIXES, tokenization
import pandas as pd


def stemming(tokens, features):
    """
    filter out prefixes from words
    :param words_list: list of words from text as [(word,count)...]
    :param prefixes: prefixes
    :return: filtered words
    """
    new_tokens = []

    # delete two heh haydiaa: e.g: הנחל הגדול -> נחל גדול
    for token in tokens:
        word1, word2 = token.split(' ')
        if word1[0] == 'ה' and word2[0] == 'ה':
            new_token = word1[1:] + ' ' + word2[1:]
            if in_sorted_list(new_token, features):
                new_tokens.append(new_token)
        elif in_sorted_list(token, features):
            new_tokens.append(token)

    final_tokens = []

    # delete prefixes
    for token in new_tokens:
        if token[0] in BI_PREFIXES and in_sorted_list(token[1:], features):
            final_tokens.append(token[1:])
        elif in_sorted_list(token, features):
            final_tokens.append(token)

    return final_tokens


def vector_of_user(text):
    filepath = "bigrams_features.json"

    features = get_features(filepath)

    # Tokenization
    tokens = tokenization(text)

    # Stemming
    stemmed_tokens = stemming(tokens, features)

    # Create vector according to the features of the texts
    vec_dict = dict((f, 0) for f in features)
    for token in stemmed_tokens:
        vec_dict[token] += 1

    final_vec = pd.Series(vec_dict)
    return final_vec


def main():
    print(vector_of_user("שלום, שמי ענבל משעל מהים לשם צפונה דרומה הדרום הצפון הים המעיין הגלים הדרום"))


if __name__ == '__main__':
    main()
