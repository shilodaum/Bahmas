from collections import Counter
from functools import partial

from super_vector import SuperVector
from vectorizer.unigram_texts_vectorizer import get_features, tokenization, SUFFIXES, PREFIXES
import pandas as pd


def stemming(tokens, features):
    # delete prefixes
    new_tokens = []
    for token in tokens:
        if token in features:
            new_tokens.append(token)
        elif token[:1] in PREFIXES and token[1:] in features:
            new_tokens.append(token[1:])
        elif token[:2] in PREFIXES and token[2:] in features:
            new_tokens.append(token[2:])

    # delete suffixes
    final_tokens = []
    for token in new_tokens:
        if token in features:
            final_tokens.append(token)
        elif token[-1:] in SUFFIXES and token[:-1] in features:
            final_tokens.append(token[:-1])
        elif token[-2:] in SUFFIXES and token[:-2] in features:
            final_tokens.append(token[:-2])

    return final_tokens


def vector_of_user(text):
    filepath = "bigrams_features.json"

    features = get_features(filepath)

    # Tokenization
    tokens = tokenization(text)

    super_vec = SuperVector.parse(list(reversed(tokens)))

    super_vec.apply_manipulation(partial(stemming, features=features))

    super_vec.apply_manipulation(Counter)

    def add_missing_features(d):
        features_dict = {f: 0 for f in features}
        return {**features_dict, **d}

    super_vec.apply_manipulation(add_missing_features)

    # final_vec = pd.Series(vec_dict)
    super_vec.apply_manipulation(pd.Series)

    # return final_vec
    return super_vec


def main():
    print(vector_of_user("שלום, שמי ענבל משעל מהים לשם צפונה דרומה הדרום הצפון הים המעיין הגלים הדרום"))


if __name__ == '__main__':
    main()
