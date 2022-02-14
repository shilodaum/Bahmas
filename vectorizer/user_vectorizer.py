from collections import Counter
from functools import partial

from super_vector import SuperVector
from vectorizer.texts_vectorizer import get_features, tokenization, SUFFIXES, PREFIXES
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
    features = get_features()

    # Tokenization
    tokens = tokenization(text)

    super_vec = SuperVector.parse(list(reversed(tokens)))

    super_vec.apply_manipulation(partial(stemming, features=features))

    # # Stemming
    # stemmed_tokens = stemming(tokens, features)

    # # Create vector according to the features of the texts
    # vec_dict = dict((f, 0) for f in features)
    # for token in stemmed:
    #     vec_dict[token] += 1

    super_vec.apply_manipulation(Counter)

    # final_vec = pd.Series(vec_dict)
    super_vec.apply_manipulation(pd.Series)

    # return final_vec
    return super_vec


def main():
    print(vector_of_user("שלום, שמי ענבל משעל מהים לשם צפונה דרומה הדרום הצפון הים המעיין הגלים הדרום"))


if __name__ == '__main__':
    main()
