import pandas as pd
import os
import json
import pickle
import numpy as np
import vectorizer.utils
from vectorizer.utils import in_sorted_list, BI_PREFIXES
import bisect

from sklearn.feature_extraction.text import CountVectorizer

directory= 'vectorizer'

def count_vectorization_bigram(df):
    vec = CountVectorizer(stop_words=vectorizer.utils.get_stop_words(), ngram_range=(2, 2))

    # fit the countVectorizer on the train's features
    train = vec.fit_transform(df)
    with open('visualization/x_transformed.pickle', 'wb') as f:
        pickle.dump(train, f)
    X_train = pd.DataFrame(train.toarray(), columns=vec.get_feature_names())

    return X_train


def stemming(df):
    """
    filter out prefixes from words
    :param words_list: list of words from text as [(word,count)...]
    :param prefixes: prefixes
    :return: filtered words
    """
    print(f'there are {len(df.columns)} couples')

    features = list(df.columns)
    features_to_delete = list()

    # delete two heh haydiaa: e.g: הנחל הגדול -> נחל גדול
    for i, feature in enumerate(features):
        if i % 1000 == 0:
            print(f'hh for feature number {i}')

        word1, word2 = feature.split(' ')
        if word1[0] == 'ה' and word2[0] == 'ה':
            new_feature = word1[1:] + ' ' + word2[1:]
            if in_sorted_list(new_feature, df.columns) and in_sorted_list(feature, df.columns):
                if not in_sorted_list(feature, features_to_delete):
                    df.loc[:, new_feature] += df.loc[:, feature]
                    # append value in a sorted way
                    bisect.insort(features_to_delete, feature)

    df = df.drop(columns=features_to_delete)
    features = list(df.columns)
    features_to_delete = list()

    # delete prefixes
    for i, feature in enumerate(features):
        if i % 1000 == 0:
            print(f'prefixes for feature number {i}')

        for pref in BI_PREFIXES:
            if in_sorted_list(pref + feature, df.columns) and in_sorted_list(feature, df.columns):
                if not in_sorted_list(feature, features_to_delete):
                    df.loc[:, feature] += df.loc[:, pref + feature]
                    # append value in a sorted way
                    bisect.insort(features_to_delete, pref + feature)

    df = df.drop(columns=features_to_delete)

    return df


def delete_rare_features_bigram(df):
    return vectorizer.utils.delete_rare_features(df, 5)


def download_df_csv(filepath):
    print('----------start to get the texts----------')
    texts_list = vectorizer.utils.get_list_of_texts()
    print('----------start to create count vector-------------')
    df = count_vectorization_bigram(texts_list)
    print('----------start to do stemming-------------')
    df = stemming(df)
    print('----------start to delete rare feature-------------')
    df = delete_rare_features_bigram(df)
    print('----------start to normalize rows-------------')
    #TODO maybe uint
    df = df.astype(np.int8)
    # df = vectorizer.utils.normalize_rows(df)
    print('-----------------------saving to file-----------------------')
    df.to_csv(os.path.join(directory,filepath), index=False, compression='zip')


def save_features(filepath):
    df = pd.read_csv(os.path.join(directory,filepath))
    features = list(df.columns)
    with open('bigrams_features.json', 'w', encoding='utf-8') as f:
        json.dump(features, f)


def add_new_trips(json_path, df_path):
    texts_list = vectorizer.utils.get_list_of_texts(json_path)
    new_trips_df = count_vectorization_bigram(texts_list)
    original_df = pd.read_csv(df_path)
    new_df = pd.concat([original_df, new_trips_df], ignore_index=True, sort=False)
    df = stemming(new_df)
    # df = vectorizer.utils.normalize_rows(df)
    df.fillna(0)
    df.to_csv(df_path, index=False, compression='zip')


def main():
    filepath = 'texts_vectors_bigrams.zip'
    # vectorizer.utils.show_df_csv(filepath)
    # print(vectorizer.utils.get_features('bigrams_features.json'))
    download_df_csv(filepath)
    save_features(filepath)


if __name__ == '__main__':
    main()
