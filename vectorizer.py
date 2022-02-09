import pandas as pd
import os
import warnings
from sklearn.cluster import KMeans

warnings.simplefilter('ignore')
import hebrew_tokenizer as ht
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.linear_model import SGDClassifier
import re

PREFIXES = ['כש', 'שב', 'ה', 'ו', 'ב', 'ל', 'ש', 'מ', 'כ', 'וש', 'שה', 'מה', 'לה', 'בה', 'וה']
SUFFIXES = ['ים', 'י', 'ך', 'נו', 'ות', 'כם', 'כן', 'יך', 'יו', 'יה', 'ינו', 'יכם', 'יכן', 'יהם', 'יהן', 'תי', 'תם',
            'תן']
tiuli_titles_folder_path = os.path.join('titles')
maslulim_israel_titles_folder_path = os.path.join('titles_maslulim_israel')


def get_list_of_words(filename):
    with open(filename, 'r') as f:
        words = f.read()
        words_list = words.split('\n')

    expanded_words_list = words_list.copy()
    for word in words_list:
        for prefix in PREFIXES:
            new = prefix + word
            expanded_words_list.append(new)

    return expanded_words_list


def get_stop_words():
    return get_list_of_words("heb_stop_words.txt")


def tokenization(text):
    text_words = []
    tokens = ht.tokenize(text)
    for grp, token, token_num, (start_index, end_index) in tokens:
        if grp == "HEBREW":
            text_words.append(token)
    return text_words


def get_list_of_texts():
    all_txt_files = []

    # tiuli output
    txt_files = os.listdir(tiuli_titles_folder_path)
    for file in txt_files:
        with open(os.path.join(tiuli_titles_folder_path, file), 'r') as f:
            corpus = f.read()
            tokens = tokenization(corpus)
            connected_tokens = " ".join(tokens)
            all_txt_files.append(connected_tokens)

    # maslulim israel output
    txt_files = os.listdir(maslulim_israel_titles_folder_path)
    for file in txt_files:
        with open(os.path.join(maslulim_israel_titles_folder_path, file), 'r') as f:
            corpus = f.read()
            tokens = tokenization(corpus)
            connected_tokens = " ".join(tokens)
            all_txt_files.append(connected_tokens)

    return all_txt_files


def count_vectorization(df):
    vec = CountVectorizer(stop_words=get_stop_words())

    # fit the countVectorizer on the train's features
    train = vec.fit_transform(df)

    X_train = pd.DataFrame(train.toarray(), columns=vec.get_feature_names())

    return X_train, train


def stemming(df):
    """
    filter out prefixes from words
    :param words_list: list of words from text as [(word,count)...]
    :param prefixes: prefixes
    :return: filtered words
    """
    features = list(df.columns)

    # delete prefixes
    for pref in PREFIXES:
        for feature in features:
            if pref + feature in df.columns and feature in df.columns:
                df.loc[:, feature] += df.loc[:, pref + feature]
                df = df.drop(columns=[pref + feature])

    features = list(df.columns)

    # delete suffixes
    for suff in SUFFIXES:
        for feature in features:
            if feature + suff in df.columns and feature in df.columns:
                df.loc[:, feature] += df.loc[:, feature + suff]
                df = df.drop(columns=[feature + suff])

    return df


def delete_rare_words(df, threshold=5):
    features = list(df.columns)
    to_del = []
    for feature in features:
        if sum(df.loc[:, feature]) < threshold:
            to_del.append(feature)

    df = df.drop(columns=to_del)
    return df


def download_df_csv():
    texts_list = get_list_of_texts()
    df, transformed = count_vectorization(texts_list)
    df = stemming(df)
    df = delete_rare_words(df)
    df.to_csv('texts_vectors.csv', index=False)


def get_features(filepath):
    df = pd.read_csv(filepath)
    return list(df.columns)


def show_df_csv(filepath):
    df = pd.read_csv(filepath)
    print(df)


def main():
    # download_df_csv('texts_vectors.csv')
    print(get_features('texts_vectors.csv'))


if __name__ == '__main__':
    main()
