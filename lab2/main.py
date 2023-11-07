import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def geomean(arr):  # середнє геометричне
    return np.exp(np.log(arr).mean())


# компонента власного вектору матриці (середнє значення оцінок пріоритетності)
def priority_makrs_avg(matrix):
    result = []

    for array in matrix:
        result.append(geomean(array))

    return result


# нормований вектор матриці попарних порівнянь (вектор пріоритетів)
def priority_vector(arr):
    result = []

    sum = np.sum(arr)

    for w in arr:
        result.append(w/sum)

    return result 

def main():
    df = pd.read_excel('lab_2_saptr.xlsx', sheet_name='first_step',
                       header=None, skiprows=3, usecols="B:D", nrows=4)
    k1 = pd.read_excel('lab_2_saptr.xlsx', sheet_name='second_step',
                       header=None, skiprows=4, usecols="C:F", nrows=5)
    k2 = pd.read_excel('lab_2_saptr.xlsx', sheet_name='second_step',
                       header=None, skiprows=12, usecols="C:F", nrows=5)
    k3 = pd.read_excel('lab_2_saptr.xlsx', sheet_name='second_step',
                       header=None, skiprows=20, usecols="C:F", nrows=5)

    matrix = df.to_numpy()[0:3]
    sum_row = df.to_numpy()[3]

    k1_matrix = k1.to_numpy()[0:4]
    k1_sum = k1.to_numpy()[4]

    k2_matrix = k2.to_numpy()[0:4]
    k2_sum = k2.to_numpy()[4]

    k3_matrix = k3.to_numpy()[0:4]
    k3_sum = k3.to_numpy()[4]

    priority_vectors = priority_vector(priority_makrs_avg(matrix))

    k1_priority_vectors = priority_vector(priority_makrs_avg(k1_matrix))
    k2_priority_vectors = priority_vector(priority_makrs_avg(k2_matrix))
    k3_priority_vectors = priority_vector(priority_makrs_avg(k3_matrix))

    final_matrix = []

    for i in range(len(k1_priority_vectors)):
        final_matrix.append([k1_priority_vectors[i],k2_priority_vectors[i],k3_priority_vectors[i]])

    result = np.matmul(np.matrix(final_matrix), np.array(priority_vectors))

    data = pd.DataFrame(result, columns = ['A','B','C','D'])

    print(data)

    plt.figure()
    sns.barplot(data=data)
    plt.show()

if __name__ == "__main__":
    main() 