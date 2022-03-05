import pandas as pd

from searcher.searcher import BaseSearcherInArray
from vectorizer.unigram_user_vectorizer import vector_of_user

world = pd.read_csv('../vectorizer/texts_vectors_unigrams.csv').to_numpy()
vector = vector_of_user("מסלול מעגלי קצר בקרבת נחל").to_numpy()

searcher = BaseSearcherInArray(vector, world)
print(searcher.search())