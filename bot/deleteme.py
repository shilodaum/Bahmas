import pandas as pd
import os

if not os.getcwd().endswith('Bahmas'):
    os.chdir('./..')

import vectorizer.unigram_user_vectorizer as uni_user
import vectorizer.bigram_user_vectorizer as bi_user
import matcher.matcher as matcher
import json


def get_data(index):
    file = open('createDB/paths_data.json')
    data = json.load(file)
    path = data[index]
    return path['path_name'], path['path_links'], path['path_description'], path['images_links'], path['map_link']


if __name__ == '__main__':
    user_input = "טיול ג'יפים בדרום"
    print('--------------reading worlds--------------')
    uni_world = pd.read_csv('vectorizer/texts_vectors_unigrams.zip')
    bi_world = pd.read_csv('vectorizer/texts_vectors_bigrams.zip')
    print('--------------building user vectors--------------')

    uni_vector = uni_user.vector_of_user(user_input)
    bi_vector = bi_user.vector_of_user(user_input)
    print('--------------search for trips--------------')
    recommendations = matcher.get_recommendation(uni_world, bi_world, uni_vector, bi_vector)

    rank = 1
    keyboard = []
    for i in recommendations:
        title, sites, description, images_links, map_link = get_data(i)
        title = title.split(":")[0]
        print(str(rank) + ": " + title)
        rank += 1
