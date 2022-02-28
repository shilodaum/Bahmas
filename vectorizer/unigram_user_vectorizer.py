from collections import Counter
from functools import partial

from super_vector import SuperVector
from vectorizer.utils import get_features, in_sorted_list, UNI_PREFIXES, UNI_SUFFIXES, tokenization
import pandas as pd


def stemming(tokens, features):
    # delete prefixes
    new_tokens = []
    for token in tokens:
        if token[:2] in UNI_PREFIXES and in_sorted_list(token[2:], features):
            new_tokens.append(token[2:])
        elif token[:1] in UNI_PREFIXES and in_sorted_list(token[1:], features):
            new_tokens.append(token[1:])
        elif in_sorted_list(token, features):
            new_tokens.append(token)

    # delete suffixes
    final_tokens = []
    for token in new_tokens:
        if token[-2:] in UNI_SUFFIXES and token[:-2] in features:
            final_tokens.append(token[:-2])
        elif token[-1:] in UNI_SUFFIXES and token[:-1] in features:
            final_tokens.append(token[:-1])
        elif token in features:
            final_tokens.append(token)

    return final_tokens


# def vector_of_user(text):
#     filepath = "unigrams_features.json"
#
#     features = get_features(filepath)
#
#     # Tokenization
#     tokens = tokenization(text)
#
#     super_vec = SuperVector.parse(list(reversed(tokens)))
#
#     super_vec.apply_manipulation(partial(stemming, features=features))
#
#     super_vec.apply_manipulation(Counter)
#
#     def add_missing_features(d):
#         features_dict = {f: 0 for f in features}
#         return {**features_dict, **d}
#
#     super_vec.apply_manipulation(add_missing_features)
#
#     # final_vec = pd.Series(vec_dict)
#     super_vec.apply_manipulation(pd.Series)
#
#     # return final_vec
#     return super_vec

def vector_of_user(text):
    filepath = "unigrams_features.json"

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
