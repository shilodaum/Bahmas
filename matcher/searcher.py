import numpy as np


class Searcher:
    def __init__(self, vector: np.ndarray, world):
        self.vector = vector
        self.existence_vector = np.where(vector != 0, 1, 0)
        self.world = world

    def jaccard_similarity(self, another_vector: np.ndarray):
        # another_existence_vector = np.where(another_vector != 0, 1, 0)
        another_existence_vector = another_vector != 0
        return self.existence_vector.dot(another_existence_vector) / len(self.existence_vector)

    def cos_similarity(self, another_vector: np.ndarray):
        return self.vector.dot(another_vector) / (np.linalg.norm(self.vector) * np.linalg.norm(another_vector))


class BaseSearcherInArray(Searcher):
    def __init__(self, vector: np.ndarray, world):
        super().__init__(vector, world)
        self.sim_func = self.cos_similarity
        # self.sim_func = self.jaccard_similarity

    def search(self):
        max_indices = sorted(list(range(len(self.world))),
                             key=lambda i: float("-inf") if np.isnan(self.sim_func(self.world[i])) else self.sim_func(
                                 self.world[i]), reverse=True)
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
