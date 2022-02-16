import json
import pickle
from sys import maxsize

from sklearn.cluster import KMeans
from wordcloud import WordCloud
from bidi.algorithm import get_display
import pandas as pd
import matplotlib.pyplot as plt

from vectorizer.texts_vectorizer import get_list_of_words


def get_titles_and_descriptions():
    file = open('../createDB/paths_data.json')
    paths_data = json.load(file)
    titles = []
    descriptions = []
    for path in paths_data:
        titles.append(path['path_name'])
        descriptions.append(path['path_description'])
    return titles, descriptions


def find_optimal_k(X_transformed, is_show=True):  # needed? not always the biggest k? maybe need to chose manually
    sum_of_squared_distances = []
    optimal_k = None
    min_ssd = maxsize
    for k in range(2, 10):
        km = KMeans(n_clusters=k, max_iter=200, n_init=10)
        km = km.fit(X_transformed)
        sum_of_squared_distances.append(km.inertia_)
        if km.inertia_ < min_ssd:
            optimal_k = k
    if is_show:
        plt.plot(range(2, 10), sum_of_squared_distances, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Sum_of_squared_distances')
        plt.title('Elbow Method For Optimal k')
        plt.show()
    return optimal_k


# https://towardsdatascience.com/clustering-documents-with-python-97314ad6a78d
def clustering(filepath):
    with open('x_transformed.pickle', 'rb') as f:
        X_transformed = pickle.load(f)
    k = 7
    model = KMeans(n_clusters=k, init='k-means++', n_init=100)
    model.fit(X_transformed)
    labels = model.labels_
    titles, descriptions = get_titles_and_descriptions()
    title_and_clusters = pd.DataFrame(list(zip(titles, labels)), columns=['title', 'cluster'])
    print(title_and_clusters.sort_values(by=['cluster']))
    create_word_clouds_of_clusters(labels, k, title_and_clusters, descriptions)


def create_word_clouds_of_clusters(labels, true_k, title_and_clusters, descriptions):
    result = {'cluster': labels, 'description': descriptions}
    result = pd.DataFrame(result)
    for k in range(0, true_k):
        s = result[result.cluster == k]
        text = s['description'].str.cat(sep=' ')
        text = ' '.join([word for word in text.split()])
        text = get_display(text)  # because Hebrew is right-to-left, we need to process the direction
        stopwords = get_list_of_words("../vectorizer/heb_stop_words.txt")
        wordcloud = WordCloud(font_path="../visualization/AdumaFont.ttf", max_font_size=50, max_words=100, background_color="white", stopwords=stopwords).generate(text)
        print('Cluster: {}'.format(k))
        print('Titles')
        titles = title_and_clusters[title_and_clusters.cluster == k]['title']
        print(titles.to_string(index=False))
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()


if __name__ == '__main__':
    clustering("../vectorizer/features.json")
