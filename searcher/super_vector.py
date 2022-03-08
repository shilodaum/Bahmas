from copy import deepcopy

import numpy as np

# connection words
and_words = ["וגם", "גם", "עם", "אך"]
or_words = ["או"]
not_words = ["ולא", "לא", "ללא", "חסר", "ובלי", "בלי"]
interpolation_words = ["interp"]

# connection map helps us understand context words
connections_map = {}
connections_map.update({word: sum for word in and_words})
# print('1: ', connections_map)
connections_map.update({word: max for word in or_words})
# print('2: ', connections_map)
connections_map.update({word: sum for word in not_words})


# print('3: ', connections_map)
def interpolation(x, y, const=0.4):
    """
    interpolate the value with a constant
    """
    return const * x + (1 - const) * y


connections_map.update({word: interpolation for word in interpolation_words})

if __name__ == '__main__':
    pass


class SuperVector:
    def __init__(self, left, right, connection):
        """
        the super vector can split the sentence into two parts - left and right
        """
        self.left = left
        self.right = right
        self.connection = connection
        self.connection_logic = None if connection is None else connections_map[connection]

    @staticmethod
    def parse(tokens):
        """
        parse the tokens of a sentence to split the sentence according to context words
        """
        connections = connections_map.keys()

        # iterate words
        for i, token in enumerate(tokens):
            if token in connections:
                # split for not words
                if token in not_words:
                    return NotSuperVector(SuperVector.parse(tokens[:i]), SuperVector.parse(tokens[i + 1:]), "וגם",
                                          token)
                return SuperVector(SuperVector.parse(tokens[:i]), SuperVector.parse(tokens[i + 1:]), token)
        return SuperVector(tokens, None, None)

    def apply_sim_func(self, sim_func):
        """
        apply similarity function between our vectors
        """
        if self.connection is None:
            return sim_func(self.left)
        left_val = self.left.apply_sim_func(sim_func)
        right_val = self.right.apply_sim_func(sim_func)

        # check invalid values
        if np.isnan(left_val):
            return right_val
        if np.isnan(right_val):
            return left_val
        return self.connection_logic(left_val, right_val)

    def apply_manipulation(self, manipulation):
        """
        apply manipulation to bith sides of the vector
        """
        if self.connection is None:
            self.left = manipulation(self.left)
        else:
            self.left.apply_manipulation(manipulation)
            self.right.apply_manipulation(manipulation)

    def reverse(self):
        """
        reverse both my right and left vector recursively
        """
        if self.connection is None:
            # Assuming called when became words counter
            self.left = (self.left == 0).astype(np.int64)
        else:
            self.left.reverse()
            self.right.reverse()

    def flip(self):
        """
        flip left value of vector
        """
        if self.connection is None:
            self.left = -self.left
        else:
            self.left.flip()
            self.right.flip()

    def __str__(self):
        """
        vector to string
        """
        if self.right is None:
            return ' '.join(self.left)
        return ' '.join([str(self.left), self.connection, str(self.right)])


class NotSuperVector(SuperVector):
    """
    a supervector with not connection
    """

    def __init__(self, left, right, connection, not_word):
        """
        constructor with super initialization
        """
        super().__init__(left, right, connection)
        self.not_word = not_word

    def apply_sim_func(self, sim_func):
        """
        apply similarity fuction with vectors
        """
        if self.connection is None:
            return sim_func(self.left == 0)

        right_copy = deepcopy(self.right)
        right_copy.flip()

        left_val = self.left.apply_sim_func(sim_func)
        right_val = right_copy.apply_sim_func(sim_func)

        # check invalid values
        if np.isnan(left_val):
            return right_val

        if np.isnan(right_val):
            return left_val

        # TODO should it be min or sum?
        if self.connection_logic is None:
            return min(left_val, right_val)
        else:
            return self.connection_logic(left_val, right_val)

    def __str__(self):
        val = super().__str__()
        return ' '.join([self.not_word, val])
