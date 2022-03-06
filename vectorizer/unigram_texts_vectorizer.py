import pandas as pd
import os
import json
import pickle
import bisect
import numpy as np
from vectorizer.utils import get_stop_words, delete_rare_features, normalize_rows, show_df_csv, \
    in_sorted_list, UNI_PREFIXES, UNI_SUFFIXES, get_list_of_texts
from sklearn.feature_extraction.text import CountVectorizer


directory = 'vectorizer'

def count_vectorization(df):
    vec = CountVectorizer(stop_words=get_stop_words())

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
    print(f'there are {len(df.columns)} words')

    features = list(df.columns)
    features_to_delete = list()
    # delete prefixes
    print('deleting prefixes')
    for i, feature in enumerate(features):
        # if i % 1000 == 0:
        #     print(f'prefixes of {i}')
        for pref in UNI_PREFIXES:
            if in_sorted_list(pref + feature, df.columns) and in_sorted_list(feature, df.columns):
                if not in_sorted_list(feature, features_to_delete):
                    df.loc[:, feature] += df.loc[:, pref + feature]
                    # append value in a sorted way
                    bisect.insort(features_to_delete, pref + feature)

    df = df.drop(columns=features_to_delete)
    features = list(df.columns)
    features_to_delete = list()

    # delete suffixes
    print('deleting suffixes')
    for i, feature in enumerate(features):
        # if i % 1000 == 0:
        #     print(f'suffixes of {i}')

        for suff in UNI_SUFFIXES:
            if in_sorted_list(feature + suff, df.columns) and in_sorted_list(feature, df.columns):
                if not in_sorted_list(feature, features_to_delete):
                    df.loc[:, feature] += df.loc[:, feature + suff]
                    bisect.insort(features_to_delete, feature + suff)
    df = df.drop(columns=features_to_delete)
    print('deleted')
    return df


def download_df_csv(filepath):
    print('-----------------------getting words-----------------------')
    texts_list = get_list_of_texts()
    print('-----------------------counting words-----------------------')
    df = count_vectorization(texts_list)
    print('-----------------------stemmming words-----------------------')
    # code for checking stemming runtime
    # start_time = time.time()

    df = stemming(df)

    # print(f'taken time {time.time() - start_time} seconds')

    print('-----------------------deleteing rare words-----------------------')
    df = delete_rare_features(df)
    print('-----------------------normalizing values-----------------------')
    df = df.astype(np.int8)
    print(df)
    print(df.dtypes)
    # df = normalize_rows(df)
    print('-----------------------saving to file-----------------------')

    df.to_csv(os.path.join(directory,filepath), index=False, compression='zip')


def save_features(filepath):
    df = pd.read_csv(os.path.join(directory,filepath))
    features = list(df.columns)
    with open('unigrams_features.json', 'w', encoding='utf-8') as f:
        json.dump(features, f)


def add_new_trips(json_path, df_path):
    texts_list = get_list_of_texts(json_path)
    new_trips_df = count_vectorization(texts_list)
    original_df = pd.read_csv(df_path)
    new_df = pd.concat([original_df, new_trips_df], ignore_index=True, sort=False)
    df = stemming(new_df)
    df = normalize_rows(df)
    df.fillna(0)
    df.to_csv(df_path, index=False, compression="zip")


# TODO correct files paths
def main():
    filepath = 'texts_vectors_unigrams.zip'
    # print(show_df_csv(filepath))
    download_df_csv(filepath)
    save_features(filepath)


if __name__ == '__main__':
    main()
