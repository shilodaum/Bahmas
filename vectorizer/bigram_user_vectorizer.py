from collections import Counter
from functools import partial
from sklearn.feature_extraction.text import CountVectorizer
from searcher.super_vector import SuperVector
from vectorizer.utils import get_features, in_sorted_list, BI_PREFIXES, tokenization
import pandas as pd


def uni_tokens_2_bi_tokens(tokens):
    """
    move from tokens of one word to tokens of words pairs
    """
    if len(tokens) < 2:
        return []
    tokens = [' '.join(tokens)]
    vec = CountVectorizer(ngram_range=(2, 2))
    vec.fit_transform(tokens)
    return vec.get_feature_names()


def stemming(tokens, features):
    """
    filter out prefixes from words
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
    """
    create bigram vector according to the user query
    """
    filepath = "bigrams_features.json"

    features = get_features(filepath)

    # Tokenization
    tokens = tokenization(text)

    # Use the super vector analysis
    super_vec = SuperVector.parse(list(reversed(tokens)))
    super_vec.apply_manipulation(uni_tokens_2_bi_tokens)
    super_vec.apply_manipulation(partial(stemming, features=features))
    super_vec.apply_manipulation(Counter)

    def add_missing_features(d):
        features_dict = {f: 0 for f in features}
        return {**features_dict, **d}

    super_vec.apply_manipulation(add_missing_features)
    super_vec.apply_manipulation(pd.Series)

    return super_vec


def main():
    # a simple try
    print(vector_of_user("שלום, שמי ענבל משעל מהים לשם צפונה דרומה הדרום הצפון הים המעיין הגלים הדרום"))


if __name__ == '__main__':
    main()
