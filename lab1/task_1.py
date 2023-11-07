import numpy as np

#Рахуємо функцію корисності
def get_utility_funcs(matrix, weights):
    utilityFuncs = []

    for row in range(len(matrix)):
        sum = 0
        for column in range(len(matrix[0])):
            sum += matrix[row][column] * weights[column]
        utilityFuncs.append(sum)

    return utilityFuncs


def main():
    matrix = np.loadtxt(open("task1.csv"), delimiter=",", max_rows=4)
    weights = np.loadtxt(open("task1.csv"), delimiter=",", skiprows=4)

    print("Matrix:")
    print(matrix)

    print("Weights:")
    print(weights)

    utilityFuncs = get_utility_funcs(matrix=matrix, weights=weights)

    print("Utility functions:")
    print(utilityFuncs)

    print("Answer:")
    print(max(utilityFuncs))


if __name__ == "__main__":
    main()
