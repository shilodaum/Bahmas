import pandas as pd

from searcher import BaseSearcherInArray
from user_vectorizer import vector_of_user

world = pd.read_csv('texts_vectors.csv').to_numpy()
vector = vector_of_user("מסלול מעגלי קצר בקרבת נחל").to_numpy()

searcher = BaseSearcherInArray(vector, world)
print(searcher.search())