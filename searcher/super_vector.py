from copy import deepcopy

import numpy as np

and_words = ["וגם", "גם", "עם", "אך"]
or_words = ["או"]
not_words = ["ולא", "לא", "ללא", "חסר", "ובלי", "בלי"]
interpolation_words = ["interp"]

connections_map = {}
connections_map.update({word: min for word in and_words})
# print('1: ', connections_map)
connections_map.update({word: max for word in or_words})
# print('2: ', connections_map)
connections_map.update({word: min for word in not_words})


# print('3: ', connections_map)
def interpolation(x, y, const=0.4):
    return const * x + (1 - const) * y


connections_map.update({word: interpolation for word in interpolation_words})

if __name__ == '__main__':
    pass


class SuperVector:
    def __init__(self, left, right, connection):
        self.left = left
        self.right = right
        self.connection = connection
        self.connection_logic = None if connection is None else connections_map[connection]

    @staticmethod
    def parse(tokens):
        connections = connections_map.keys()

        for i, token in enumerate(tokens):
            if token in connections:
                if token in not_words:
                    return NotSuperVector(SuperVector.parse(tokens[:i]), SuperVector.parse(tokens[i + 1:]), "וגם",
                                          token)
                return SuperVector(SuperVector.parse(tokens[:i]), SuperVector.parse(tokens[i + 1:]), token)
        return SuperVector(tokens, None, None)

    def apply_sim_func(self, sim_func):
        if self.connection is None:
            return sim_func(self.left)
        left_val = self.left.apply_sim_func(sim_func)
        right_val = self.right.apply_sim_func(sim_func)

        if np.isnan(left_val):
            return right_val
        if np.isnan(right_val):
            return left_val
        return self.connection_logic(left_val, right_val)

    def apply_manipulation(self, manipulation):
        if self.connection is None:
            self.left = manipulation(self.left)
        else:
            self.left.apply_manipulation(manipulation)
            self.right.apply_manipulation(manipulation)

    def reverse(self):
        if self.connection is None:
            # Assuming called when became words counter
            self.left = (self.left == 0).astype(np.int64)
        else:
            self.left.reverse()
            self.right.reverse()

    def __str__(self):
        if self.right is None:
            return ' '.join(self.left)
        return ' '.join([str(self.left), self.connection, str(self.right)])


class NotSuperVector(SuperVector):
    def __init__(self, left, right, connection, not_word):
        super().__init__(left, right, connection)
        self.not_word = not_word

    def apply_sim_func(self, sim_func):
        if self.connection is None:
            return sim_func(self.left == 0)

        left_copy = deepcopy(self.left)
        left_copy.reverse()
        right_copy = deepcopy(self.right)
        right_copy.reverse()

        left_val = left_copy.apply_sim_func(sim_func)
        right_val = right_copy.apply_sim_func(sim_func)

        if np.isnan(left_val):
            return right_val

        if np.isnan(right_val):
            return left_val

        return min(left_val, right_val)

    def __str__(self):
        val = super().__str__()
        return ' '.join([self.not_word, val])
