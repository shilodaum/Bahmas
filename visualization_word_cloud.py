import os.path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from os import path
from PIL import Image


# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def find_buzzwords(corpus):
    words = corpus.split()
    # print(words)
    words_options = set(words)
    counter = {word: words.count(word) for word in words_options}
    # print(list(counter.items()))
    sorted_buzzwords = dict_to_sorted_items(counter)
    # print(sorted_buzzwords)
    return sorted_buzzwords
    # TODO what about prefixes or close words
    # for word in words:


def get_common_words():
    return stop_words()


def find_unique_buzzwords(corpus):
    all_buzzwords = find_buzzwords(corpus)
    general_common_words = get_common_words()
    uniqe_buzzwords = list()
    for word, freq in all_buzzwords:
        if word not in general_common_words:
            uniqe_buzzwords.append((word, freq))
    return manage_prefixes(uniqe_buzzwords)


def filter_hebrew(buzzwords, symbols):
    buzzwords_dict = dict(buzzwords)
    # find only hebrew words
    for key, value in buzzwords:
        if len(key) <= 1:
            del buzzwords_dict[key]
        elif key.isnumeric():
            del buzzwords_dict[key]
        # elif key[-1] in symbols.split():
        #     buzzwords_dict[key[:-1]] = buzzwords_dict[key]
        #     del buzzwords_dict[key]
        #     if not all("\u0590" <= character <= "\u05EA" for character in key[:-1]):
        #         del buzzwords_dict[key[:-1]]
        elif key[-1] in symbols.split():
            if all("\u0590" <= character <= "\u05EA" for character in key[:-1]):
                buzzwords_dict[key[:-1]] = buzzwords_dict[key]
            del buzzwords_dict[key]

        elif not all("\u0590" <= character <= "\u05EA" for character in key):
            del buzzwords_dict[key]
    return dict_to_sorted_items(buzzwords_dict)


def filter_prefixes(buzzwords, prefixes):
    buzzwords_dict = dict(buzzwords)
    for pref in prefixes.split():
        for word, freq in buzzwords:

            if pref + word in buzzwords_dict.keys() and word in buzzwords_dict.keys():
                buzzwords_dict[word] += buzzwords_dict[pref + word]
                del buzzwords_dict[pref + word]

    return dict_to_sorted_items(buzzwords_dict)


def manage_prefixes(buzzwords, symbols='? - ! . , : ;', prefixes='ה ו ב ל ש מ כ וש שה מה לה בה וה'):
    hebrew_buzzwords = filter_hebrew(buzzwords, symbols)
    buzzwords_prefixes = filter_prefixes(hebrew_buzzwords, prefixes)
    return buzzwords_prefixes


def stop_words():
    sent = ''
    with open('heb_stop_words.txt', 'r') as f:
        sent = f.read()
    return sent.split()


def dict_to_sorted_items(d):
    return sorted(list(d.items()), key=lambda item: item[1], reverse=True)


def main():
    txt = ''
    unique = dict()
    for i in range(1, 342):
        if os.path.exists(f'titles/{i}.txt'):
            with open(f'titles/{i}.txt', 'r') as f:
                unique2 = find_unique_buzzwords(f.read())
                for key, value in unique2:
                    if key in unique:
                        unique[key] += value
                    else:
                        unique[key] = value

    demo_text = ''
    unique_list = dict_to_sorted_items(unique)
    for key, value in unique_list:
        demo_text += (key + ' ') * value
    with open("demo_text.txt", 'w') as f:
        f.write(demo_text)

    print(unique_list)


if __name__ == '__main__':
    main()
