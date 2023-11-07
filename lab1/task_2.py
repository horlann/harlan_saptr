import numpy as np

#Нормалізуємо матрицю
def normalize_matrix(matrix):

    for column in range(len(matrix[0])):
        temp = []

        for row in range(len(matrix)):
            temp.append(matrix[row][column])

        for row in range(len(matrix)):

            if column in minimizeIndexes:
                matrix[row][column] = (max(temp) - matrix[row][column]
                                       ) / (max(temp) - min(temp))
            else:
                matrix[row][column] = (
                    (matrix[row][column] - min(temp)) / (max(temp) - min(temp)))
    return matrix


def get_utility_funcs(matrix, weights):
    utilityFuncs = []

    for row in range(len(matrix)):
        result = 0

        for column in range(len(matrix[0])):
            result += matrix[row][column] * weights[column]

        utilityFuncs.append(result)

    return utilityFuncs


matrix = np.loadtxt(open("task2.csv"), delimiter=",", max_rows=5)
weights = np.loadtxt(open("task2.csv"), delimiter=",", skiprows=5)

minimizeIndexes = [1]

print("Matrix:")
print(matrix)

print("Weights:")
print(weights)

matrix = normalize_matrix(matrix=matrix)

print("Normalized matrix:")
print(matrix)

print("Utility functions:")
print(get_utility_funcs(matrix=matrix, weights=weights))

print("Answer:")
print(max(get_utility_funcs(matrix=matrix, weights=weights)))
