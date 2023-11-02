import numpy as np


def pearson_correlation(x, y):
    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)

    sum_xy = sum(map(lambda a, b: a * b, x, y))

    sum_x_squared = sum(map(lambda a: a ** 2, x))
    sum_y_squared = sum(map(lambda a: a ** 2, y))

    numerator = (n * sum_xy) - (sum_x * sum_y)

    denominator = np.sqrt((n * sum_x_squared - sum_x ** 2) * (n * sum_y_squared - sum_y ** 2))

    if denominator == 0:
        return 0.0
    else:
        return numerator / denominator


x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

correlation = pearson_correlation(x, y)
print(correlation)
