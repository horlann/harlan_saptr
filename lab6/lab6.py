import numpy as np
from scipy.optimize import linear_sum_assignment


def main():

    matrix = np.array([
    [46, 59, 24, 62, 67],
    [47, 56, 32, 55, 70],
    [44, 52, 19, 61, 60],
    [47, 59, 17, 64, 73],
    [43, 65, 20, 60, 75]
    ])

    row_ind, col_ind = linear_sum_assignment(matrix)
    result = []
    sum=0

    for i in range(len(matrix[0])):
        sum+=matrix[i][col_ind[i]]
        result.append(matrix[i][col_ind[i]])

    print(result)
    print(sum)


main()