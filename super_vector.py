import numpy as np


class SuperVector:
    def __init__(self, left, right, connection):
        self.left = left
        self.right = right
        self.connection = connection
        self.connection_logic = None if connection is None else {"או": max, "וגם": min}[connection]

    @staticmethod
    def parse(tokens):
        connections = ["או", "וגם"]

        for i, token in enumerate(tokens):
            if token in connections:
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

    def __str__(self):
        if self.right is None:
            return ' '.join(self.left)
        return ' '.join([str(self.left), self.connection, str(self.right)])
