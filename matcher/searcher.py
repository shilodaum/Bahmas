from functools import partial

import numpy as np


class Searcher:
    def __init__(self, super_vector, world):
        self.super_vector = super_vector
        self.world = world

    @staticmethod
    def jaccard_similarity(vector1: np.array, vector2: np.array):
        existence_vector1 = vector1 != 0
        existence_vector2 = vector2 != 0
        return existence_vector1.dot(existence_vector2) / len(existence_vector1)

    @staticmethod
    def cos_similarity(vector1: np.array, vector2: np.array):
        return vector1.dot(vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))


class BaseSearcherInArray(Searcher):
    def __init__(self, super_vector, world):
        super().__init__(super_vector, world)
        self.sim_func = self.cos_similarity
        # self.sim_func = self.jaccard_similarity

    def search(self):
        def key_func(vec):
            partial_func = partial(self.sim_func, vec)
            val = self.super_vector.apply_sim_func(partial_func)
            return val if not np.isnan(val) else float("-inf")

        max_indices = sorted(list(range(len(self.world))),
                             key=key_func, reverse=True)
        return max_indices[:5]

# class AdamSearcher:
#     def __init__(self, vector: np.ndarray, world):
#         self.vector = vector
#         self.sim_func = partial(reduce, lambda v, f: f(v), [partial(cosine_similarity, self.vector), tf.math.abs])
#         self.world = world
#
#     @staticmethod
#     def num_to_2_vec(num):
#         first_i = tf.math.divide(tf.math.log(num), math.log(2))
#         i = first_i
#         vec = []
#
#         while True:
#             if num >= 2 ** i:
#                 vec.append(1)
#                 num >>= i
#             else:
#                 vec.append(0)
#
#             if i == 0:
#                 break
#             i >>= 1
#
#         return list(reversed(vec))
#
#     def search(self):
#         optimizer = Adam()
#         loss_val = constant(float("inf"))
#         threshold = 0.1
#
#         to_train = constant(1)
#
#         while loss_val > threshold:
#             as_vec = constant(AdamSearcher.num_to_2_vec(to_train), dtype='float32')
#             print(type(as_vec))
#             print(as_vec)
#             with GradientTape() as tape:
#                 tape.watch(as_vec)
#                 loss_value = self.sim_func(as_vec)
#
#             # Get gradients of loss wrt the weights.
#             gradients = tape.gradient(loss_value, to_train)
#
#             print(gradients)
#
#             # Update the weights of the model.
#             optimizer.apply_gradients(zip(gradients, to_train))
#
#         return num_to_2_vec(int(to_train))
#
#
