from functools import partial

import numpy as np

from searcher.super_vector import interpolation


class Searcher:
    def __init__(self, super_vector, world):
        """
        initialize the searcher class with the super vector and the whole data (=world)
        """
        self.super_vector = super_vector
        self.world = world

    @staticmethod
    def jaccard_similarity(vector1: np.array, vector2: np.array):
        """
        calculate the similarity between the vectors using jaccard_similarity
        """
        existence_vector1 = vector1 != 0
        existence_vector2 = vector2 != 0
        return existence_vector1.dot(existence_vector2) / len(existence_vector1)

    @staticmethod
    def cos_similarity(vector1: np.array, vector2: np.array):
        """
        calculate the similarity between the vectors using cos_similarity
        """
        return vector1.dot(vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))


class BaseSearcherInArray(Searcher):
    def __init__(self, super_vector, world):
        """
        initialize the class with the super vector, the whole data (=world) and the chosen similarity method
        """
        super().__init__(super_vector, world)
        self.sim_func = self.cos_similarity
        # self.sim_func = self.jaccard_similarity

    def search(self):
        """
        returns the 5 most recommended paths
        """

        def key_func(index):
            """
            calculate the distance from the vectors
            """
            partial_func = partial(self.sim_func, self.world[index])
            val = self.super_vector.apply_sim_func(partial_func)
            return val if not np.isnan(val) else float("-inf")

        # find the best paths
        max_indices = sorted(list(range(len(self.world))),
                             key=key_func, reverse=True)
        return max_indices[:5]


class InterpolationSearcher(Searcher):
    def __init__(self, super_vector, world1, world2):
        """
        initialize the class with the super vector, the whole data of unigram and bigram
         and the chosen similarity method
        """
        super().__init__(super_vector, (world1, world2))
        self.sim_func = self.cos_similarity
        # self.sim_func = self.jaccard_similarity

    def search(self):
        """
        returns the 5 most recommended paths
        """

        def key_func(index):
            """
            calculate the similarity between the unigram vectors and the bigram vectors
            """
            partial_func_1 = partial(self.sim_func, self.world[0].iloc[index])
            partial_func_2 = partial(self.sim_func, self.world[1].iloc[index])
            val1 = self.super_vector.left.apply_sim_func(partial_func_1)
            val2 = self.super_vector.right.apply_sim_func(partial_func_2)

            # edge cases
            if np.isnan(val1):
                if np.isnan(val2):
                    return float("-inf")
                return val2
            if np.isnan(val2):
                return val1

            # interpolate the 2 values
            return interpolation(val1, val2)

        # find the paths with the highest scores
        recommendations = [(ind, key_func(ind)) for ind in range(self.world[0].shape[0])]
        sorted_rec = sorted(recommendations, key=lambda el: el[1], reverse=True)
        return [el[0] for el in sorted_rec], [el[1] for el in sorted_rec]
