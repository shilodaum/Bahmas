import os
from collections import Counter
from functools import partial
from textwrap import wrap

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from searcher.searcher import BaseSearcherInArray
from searcher.super_vector import SuperVector
from vectorizer.unigram_texts_vectorizer import stemming as stemming_text
from vectorizer.unigram_texts_vectorizer import count_vectorization
from vectorizer.unigram_user_vectorizer import stemming
from vectorizer.utils import tokenization, delete_rare_features

if 'Bahmas' in os.getcwd():
    if not os.getcwd().endswith('Bahmas'):
        os.chdir('..')
    directory = os.getcwd()
else:
    directory = "/app"
all_paths = pd.read_json(os.path.join(directory, 'createDB', 'paths_data.zip'))


def get_features():
    data = all_paths.iloc[:10]['path_description']

    all_txt_files = [" ".join(tokenization(element)) for element in data]

    features = count_vectorization(all_txt_files)

    features = stemming_text(features)

    features = delete_rare_features(features)
    features = features.astype(np.int8)

    return features


def vector_of_user(text, features):
    # Tokenization
    tokens = tokenization(text)

    super_vec = SuperVector.parse(list(reversed(tokens)))

    super_vec.apply_manipulation(partial(stemming, features=list(features.keys())))

    super_vec.apply_manipulation(Counter)

    def add_missing_features(d):
        features_dict = {f: 0 for f in features}
        return {**features_dict, **d}

    super_vec.apply_manipulation(add_missing_features)

    # final_vec = pd.Series(vec_dict)
    super_vec.apply_manipulation(pd.Series)

    # return final_vec
    return super_vec


features = get_features()
queries = [
    "הר וגם אגם",
    "טיול למשפחות בחרמון",
    "טיול הררי ברמת הגולן עם נוף יפה",
    "טיול מעגלי באילת",
    "טיול משפחות בנחל",
    "טיול משפחות בחדרה",
    "נחל עם מבצר",
    "הר וגם יער",
    "אני רוצה לטייל ביער",
    "נחל אלכסנדר"
]

recommendations = []
for query in queries:
    vector = (vector_of_user(query, features))
    searcher = BaseSearcherInArray(vector, features)
    recommendations.append(searcher.search())

print(recommendations)


def plot(queries, recommendations):
    # '\n'.join(el[::-1] for el in wrap(all_paths.iloc[i]['path_name'], 20))

    reversed_queries = ['\n'.join(el[::-1] for el in wrap(word, 10)) for word in queries]
    recs_texts = all_paths.iloc[:10]['path_name']
    reversed_recs = ['\n'.join(el[::-1] for el in wrap(word, 20)) for word in recs_texts]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.tick_params(axis='both', labelsize=8)
    ax.set_xticks(np.arange(len(reversed_queries)), labels=reversed_queries, rotation=45)
    ax.set_yticks(np.arange(len(reversed_recs)), labels=reversed_recs)

    plt.rc('font', size=8)

    indexed_scores = [list(enumerate(recommendations[j][1])) for j in range(len(recommendations))]
    indexed_scores = [list(sorted(indexed_scores[j], key=lambda i: recommendations[j][0][i[0]])) for j in range(len(recommendations))]

    scores = [[el[1] for el in scores_arr] for scores_arr in indexed_scores]

    for i in range(len(reversed_queries)):
        for j in range(len(reversed_recs)):
            ax.text(i, j, round(scores[i][j], 4),
                    ha="center", va="center", color="g")

    scores = np.array(scores)
    plt.imshow(scores.T, cmap='GnBu', interpolation='nearest')
    plt.show()


plot(queries, recommendations)

