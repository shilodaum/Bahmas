import warnings

warnings.simplefilter('ignore')
import json
import os
import time
import bisect

import hebrew_tokenizer as ht
import pandas as pd

if 'Bahmas' in os.getcwd():
    if not os.getcwd().endswith('Bahmas'):
        os.chdir('..')
    directory = os.getcwd()
else:
    directory = "/app"


UNI_PREFIXES = ['כש', 'שב', 'ה', 'ו', 'ב', 'ל', 'ש', 'מ', 'כ', 'וש', 'שה', 'מה', 'לה', 'בה', 'וה']
UNI_SUFFIXES = ['ים', 'י', 'ך', 'נו', 'ות', 'כם', 'כן', 'יך', 'יו', 'יה', 'ינו', 'יכם', 'יכן', 'יהם', 'יהן', 'תי', 'תם',
                'תן']
BI_PREFIXES = ['ה', 'ו', 'ב', 'ל', 'ש', 'מ', 'כ']

# we used this function in order to optimize the functions runtime
def timeit(f):
    """
    gives us the running time of each function.
    """
    def inside(*args):
        start_time = time.time()
        f(*args)
        print(f'taken time {time.time() - start_time} seconds')

    return inside


def get_stop_words():
    """
    returns a list of the hebrew stop words
    """
    return get_list_of_words("vectorizer/heb_stop_words.txt")


def delete_rare_features(df, threshold=5):
    """
    delete rare features according to a chosen threshold
    """
    features = list(df.columns)
    to_del = []
    for feature in features:
        if sum(df.loc[:, feature]) < threshold:
            to_del.append(feature)

    df = df.drop(columns=to_del)
    return df


def show_df_csv(filepath):
    """
    prints the data frame from a given path
    """
    df = pd.read_csv(filepath)
    print(df)


def get_features(filepath):
    """
    get the features list from the file in the filepath
    """
    with open(os.path.join(directory, 'vectorizer', filepath), 'r', encoding='utf-8') as f:
        features = json.load(f)
    return features


def in_sorted_list(elem, sorted_list):
    """
    using bisect algorithm find if value is in an array, i is the index in which i want to insert my value
    """
    i = bisect.bisect_left(sorted_list, elem)
    return i != len(sorted_list) and sorted_list[i] == elem


def get_list_of_words(filename):
    """
    read a list of words and expand it according to the prefixes
    """
    with open(filename, 'r') as f:
        words = f.read()
        words_list = words.split('\n')

    expanded_words_list = words_list.copy()
    for word in words_list:
        for prefix in UNI_PREFIXES:
            new = prefix + word
            expanded_words_list.append(new)

    return expanded_words_list


def get_list_of_texts(json_path=os.path.join('createDB', 'paths_data.json')):
    """
    returns list of the websites texts after tokenization
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        elements_list = json.load(f)
        all_txt_files = [" ".join(tokenization(element['path_description'])) for element in elements_list]

    return all_txt_files


def tokenization(text):
    """
    filter only the hebrew words from the text using hebrew tokenizer
    """
    text_words = []
    tokens = ht.tokenize(text)
    for grp, token, token_num, (start_index, end_index) in tokens:
        if grp == "HEBREW":
            text_words.append(token)
    return text_words
