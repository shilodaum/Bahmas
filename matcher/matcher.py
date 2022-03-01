# Get two user vectors - one of uni and one of bi and get the sim-coef. Then get the rate.
import pandas as pd
import numpy as np


def jaccard_similarity(vec1, vec2):
    vec1 = vec1.to_numpy()
    vec2 = vec2.to_numpy()

    existence_vector1 = vec1 != 0
    existence_vector2 = vec2 != 0
    return existence_vector1.dot(existence_vector2) / len(existence_vector1)


def cos_similarity(vec1, vec2):
    vec1 = vec1.to_numpy()
    vec2 = vec2.to_numpy()

    return vec1.dot(vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def dist_interpolation(uni_dist, bi_dist, uni_weight=0.4):
    return uni_weight * uni_dist + (1 - uni_weight) * bi_dist


def calc_world_dist(world, user_vector, dist_method):
    def calc_dist_row(row):
        return dist_method(row, user_vector)

    return world.apply(calc_dist_row, axis=1)


def calc_world_dist_bi_and_uni(world1, world2, user_uni_vector, user_bi_vector, dist_method=cos_similarity):
    uni_dist_vec = calc_world_dist(world1, user_uni_vector, dist_method)
    bi_dist_vec = calc_world_dist(world2, user_bi_vector, dist_method)

    return dist_interpolation(uni_dist_vec, bi_dist_vec, uni_weight=0.4)


def get_recommendation(world1, world2, user_uni_vector, user_bi_vector, dist_method=cos_similarity):
    dist_vec = calc_world_dist_bi_and_uni(world1, world2, user_uni_vector, user_bi_vector, dist_method=cos_similarity)

    max_indices = np.argsort(dist_vec.to_numpy())

    return max_indices[-5:]
