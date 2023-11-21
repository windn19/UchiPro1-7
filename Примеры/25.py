import math


class Point:
    MAX_SIZE = 10

    @staticmethod
    def get_distance(x, y):
        return math.sqrt(x ** 2 + y ** 2)


print(Point.get_distance(-2, -2))  # 2.8284271247461903
