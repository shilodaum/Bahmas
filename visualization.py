from sys import maxsize

from sklearn.cluster import KMeans
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt


def get_features(filepath):
    df = pd.read_csv(filepath)
    return list(df.columns)


def find_optimal_k(X_transformed, is_show=True):
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
def clustering(X_transformed, filepath):
    k = find_optimal_k(X_transformed, is_show=True)
    model = KMeans(n_clusters=k, init='k-means++', n_init=100)
    model.fit(X_transformed)
    model.fit(X_transformed)
    labels = model.labels_
    title = get_features(filepath)
    title_and_clusters = pd.DataFrame(list(zip(title, labels)), columns=['title', 'cluster'])
    print(title_and_clusters.sort_values(by=['cluster']))
    create_word_clouds_of_clusters()


def create_word_clouds_of_clusters(labels, true_k, title_and_clusters):
    result = {'cluster': labels, 'wiki': wiki_lst}
    result = pd.DataFrame(result)
    for k in range(0, true_k):
        s = result[result.cluster == k]
        text = s['wiki'].str.cat(sep=' ')
        text = text.lower()
        text = ' '.join([word for word in text.split()])
        wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
        print('Cluster: {}'.format(k))
        print('Titles')
        titles = title_and_clusters[title_and_clusters.cluster == k]['title']
        print(titles.to_string(index=False))
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()
