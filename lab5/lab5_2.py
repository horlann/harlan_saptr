import numpy as np


def get_minmax(matrix):
    transpose_matrix = matrix.T

    cols_min_values = []

    for col in transpose_matrix:
        cols_min_values.append(np.max(col))

    cols_min_values.append(get_maxmin(matrix))

    return np.min(cols_min_values)


def get_maxmin(matrix):
    rows_min_values = []

    for row in matrix:
        rows_min_values.append(np.min(row))

    return np.max(rows_min_values)


def main():
    matrix = np.array([
        [0.9, 0.4, 0.2],
        [0.3, 0.6, 0.8],
        [0.5, 0.7, 0.2]
    ])

    print(get_minmax(matrix))
    print(get_maxmin(matrix))


if __name__ == '__main__':
    main()