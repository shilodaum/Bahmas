import pandas as pd
import os
import warnings
import json
import pickle

warnings.simplefilter('ignore')
import hebrew_tokenizer as ht
from sklearn.feature_extraction.text import CountVectorizer

import unigram_texts_vectorizer as unigram_vec
PREFIXES = ['כש', 'שב', 'ה', 'ו', 'ב', 'ל', 'ש', 'מ', 'כ', 'וש', 'שה', 'מה', 'לה', 'בה', 'וה']
SUFFIXES = ['ים', 'י', 'ך', 'נו', 'ות', 'כם', 'כן', 'יך', 'יו', 'יה', 'ינו', 'יכם', 'יכן', 'יהם', 'יהן', 'תי', 'תם',
            'תן']
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


def delete_rare_features_bigram(df):
    return unigram_vec.delete_rare_features(df, 5)

def download_df_csv(filepath):
    texts_list = unigram_vec.get_list_of_texts()
    df = count_vectorization_bigram(texts_list)
    df = delete_rare_features_bigram(df)
    df = delete_rare_features_bigram(df)
    df = unigram_vec.normalize_rows(df)
    df.to_csv(filepath, index=False)

def save_features(filepath):
    df = pd.read_csv(filepath)
    features = list(df.columns)
    with open('features_bigrams.json', 'w', encoding='utf-8') as f:
        json.dump(features, f)

def main():
    filepath = 'texts_vectors_bigrams.csv'
    # unigram_vec.show_df_csv(filepath)
    print(unigram_vec.get_features('features_bigrams.json'))
    # download_df_csv(filepath)
    # save_features(filepath)

if __name__ == '__main__':
    main()
