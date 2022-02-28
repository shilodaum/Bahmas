import pandas as pd
import os
import warnings
import json
import pickle

warnings.simplefilter('ignore')
import hebrew_tokenizer as ht
from sklearn.feature_extraction.text import CountVectorizer

import unigram_texts_vectorizer as unigram_vec
PREFIXES = ['ה', 'ו', 'ב', 'ל', 'ש', 'מ', 'כ']
tiuli_titles_folder_path = os.path.join('titles_tiuli')
maslulim_israel_titles_folder_path = os.path.join('titles_maslulim_israel')



def count_vectorization_bigram(df):
    vec = CountVectorizer(stop_words=unigram_vec.get_stop_words(), ngram_range=(2, 2))

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

    print(len(features), ' features:')

    # delete two heh haydiaa: e.g: הנחל הגדול -> נחל גדול
    for i, feature in enumerate(features):
        if i % 1000 == 0:
            print('feature number ', i)

        word1, word2 = feature.split(' ')
        if word1[0] == 'ה' and word2[0] == 'ה':
            new_feature = word1[1:] + ' ' + word2[1:]
            if new_feature in df.columns and feature in df.columns:
                df.loc[:, new_feature] += df.loc[:, feature]
                df = df.drop(columns=[feature])

    # delete prefixes
    for pref in PREFIXES:
        for feature in features:
            if pref + feature in df.columns and feature in df.columns:
                df.loc[:, feature] += df.loc[:, pref + feature]
                df = df.drop(columns=[pref + feature])

    return df

def delete_rare_features_bigram(df):
    return unigram_vec.delete_rare_features(df, 5)

def download_df_csv(filepath):
    print('----------start to get the texts----------')
    texts_list = unigram_vec.get_list_of_texts()
    print('----------start to create count vector-------------')
    df = count_vectorization_bigram(texts_list)
    print('----------start to do stemming-------------')
    df = stemming(df)
    print('----------start to delete rare feature-------------')
    df = delete_rare_features_bigram(df)
    print('----------start to normalize rows-------------')
    df = unigram_vec.normalize_rows(df)
    df.to_csv(filepath, index=False)

def save_features(filepath):
    df = pd.read_csv(filepath)
    features = list(df.columns)
    with open('bigrams_features.json', 'w', encoding='utf-8') as f:
        json.dump(features, f)

def main():
    filepath = 'texts_vectors_bigrams.csv'
    # unigram_vec.show_df_csv(filepath)
    # print(unigram_vec.get_features('bigrams_features.json'))
    download_df_csv(filepath)
    # save_features(filepath)

if __name__ == '__main__':
    main()
