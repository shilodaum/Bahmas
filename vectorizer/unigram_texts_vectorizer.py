import pandas as pd
import os
import warnings
import json
import pickle

warnings.simplefilter('ignore')
import hebrew_tokenizer as ht
from sklearn.feature_extraction.text import CountVectorizer

PREFIXES = ['כש', 'שב', 'ה', 'ו', 'ב', 'ל', 'ש', 'מ', 'כ', 'וש', 'שה', 'מה', 'לה', 'בה', 'וה']
SUFFIXES = ['ים', 'י', 'ך', 'נו', 'ות', 'כם', 'כן', 'יך', 'יו', 'יה', 'ינו', 'יכם', 'יכן', 'יהם', 'יהן', 'תי', 'תם',
            'תן']
tiuli_titles_folder_path = os.path.join('titles_tiuli')
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
    return get_list_of_words("./heb_stop_words.txt")


def tokenization(text):
    text_words = []
    tokens = ht.tokenize(text)
    for grp, token, token_num, (start_index, end_index) in tokens:
        if grp == "HEBREW":
            text_words.append(token)
    return text_words


def get_list_of_texts():
    all_txt_files = []

    with open(os.path.join('..', 'createDB', 'paths_data.json'), 'r', encoding='utf-8') as f:
        elements_list = json.load(f)
        all_txt_files = [" ".join(tokenization(element['path_description'])) for element in elements_list]

    return all_txt_files


def count_vectorization(df):
    vec = CountVectorizer(stop_words=get_stop_words())

    # fit the countVectorizer on the train's features
    train = vec.fit_transform(df)
    with open('../visualization/x_transformed.pickle', 'wb') as f:
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


def delete_rare_features(df, threshold=5):
    features = list(df.columns)
    to_del = []
    for feature in features:
        if sum(df.loc[:, feature]) < threshold:
            to_del.append(feature)

    df = df.drop(columns=to_del)
    return df


def normalize_rows(df):
    return df.div(df.sum(axis=1), axis=0)


def download_df_csv(filepath):
    print('----------start to get the texts----------')
    texts_list = get_list_of_texts()
    print('----------start to create count vector-------------')
    df = count_vectorization(texts_list)
    print('----------start to do stemming-------------')
    df = stemming(df)
    print('----------start to delete rare feature-------------')
    df = delete_rare_features(df)
    print('----------start to normalize rows-------------')
    df = normalize_rows(df)
    df.to_csv(filepath, index=False)


def save_features(filepath):
    df = pd.read_csv(filepath)
    features = list(df.columns)
    with open('unigrams_features.json', 'w', encoding='utf-8') as f:
        json.dump(features, f)


def get_features(filepath):
    with open('../vectorizer/' + filepath, 'r', encoding='utf-8') as f:
        features = json.load(f)
    return features


def show_df_csv(filepath):
    df = pd.read_csv(filepath)
    print(df)


def main():
    filepath = 'texts_vectors_unigrams.csv'
    print(show_df_csv())
    # download_df_csv(filepath)
    # save_features(filepath)


if __name__ == '__main__':
    main()
