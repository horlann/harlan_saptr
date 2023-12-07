import numpy as np
from sklearn.preprocessing import LabelBinarizer


def relative_majority(e, votes):
    return (e[0] * votes).sum(axis=1)


def encoded(matrix, label_binarizer):
    encoded = label_binarizer.fit_transform(matrix.flatten())
    encoded = encoded.reshape(matrix.shape + (4,))
    encoded = encoded.transpose((0, 2, 1))

    return encoded


def relative(labels, e, votes):
    relative_majority_score = relative_majority(e, votes)
    relative_majority_result = labels[relative_majority_score.argmax()]
    return relative_majority_result


def absolute(labels, matrix, votes, encoded, label_binarizer):
    relative_majority_score = (encoded[0] * votes).sum(axis=1)

    sorted_result = np.sort(relative_majority_score)[-2:]
    indices = np.where(np.isin(relative_majority_score, sorted_result))[0]
    second_indicies = np.argmax(np.isin(matrix, labels[indices]), axis=0)
    top2_vector = label_binarizer.transform(
        matrix[second_indicies, np.arange(matrix.shape[1])]).T * votes
    absolute_score = top2_vector.sum(axis=1)
    absolute_result = labels[absolute_score.argmax()]

    return absolute_result


def borda(encoded, votes, labels):
    mul_array = encoded * votes
    arr_score = mul_array * np.array([3, 2, 1, 0])[:, np.newaxis, np.newaxis]
    bord_score = arr_score.sum(axis=2).sum(axis=0)
    bord_result = labels[bord_score.argmax()]

    return bord_result


def condorse(matrix, votes, labels):
    unique_chars = np.unique(matrix)
    sorted_chars = np.sort(unique_chars)

    char_to_num = {char: i for i, char in enumerate(sorted_chars)}
    num_matrix = np.vectorize(char_to_num.get)(matrix)
    matrix_cond = np.zeros((4, 4))

    for i, col in enumerate(num_matrix.T):
        for x in range(col.shape[0]):
            for y in range(x+1, col.shape[0]):
                matrix_cond[col[x]][col[y]] += votes[i]

    for i, e1 in enumerate(labels):
        winner = True
        for j in range(labels.shape[0]):
            if i != j:
                if matrix_cond[i][j] < matrix_cond[j][i]:
                    winner = False
        if winner:
            matrix_result = e1
            return matrix_result


def coplend(matrix, votes, labels):
    unique_chars = np.unique(matrix)
    sorted_chars = np.sort(unique_chars)

    char_to_num = {char: i for i, char in enumerate(sorted_chars)}
    num_matrix = np.vectorize(char_to_num.get)(matrix)
    matrix_cond = np.zeros((4, 4))

    for i, col in enumerate(num_matrix.T):
        for x in range(col.shape[0]):
            for y in range(x+1, col.shape[0]):
                matrix_cond[col[x]][col[y]] += votes[i]

    cop_score = np.zeros(matrix.shape[0])
    for i, e1 in enumerate(labels):
        for j in range(labels.shape[0]):
            if i != j:
                if matrix_cond[i][j] < matrix_cond[j][i]:
                    cop_score[i] -= 1
                elif matrix_cond[i][j] > matrix_cond[j][i]:
                    cop_score[i] += 1

    cop_result = labels[cop_score.argmax()]
    return cop_result


def simpson(matrix, votes, labels):
    unique_chars = np.unique(matrix)
    sorted_chars = np.sort(unique_chars)

    char_to_num = {char: i for i, char in enumerate(sorted_chars)}
    num_matrix = np.vectorize(char_to_num.get)(matrix)
    matrix_cond = np.zeros((4, 4))

    for i, col in enumerate(num_matrix.T):
        for x in range(col.shape[0]):
            for y in range(x+1, col.shape[0]):
                matrix_cond[col[x]][col[y]] += votes[i]

    data_no_zeros = np.where(matrix_cond == 0, np.nan, matrix_cond)

    simpson_score = np.nanmin(data_no_zeros, axis=1)

    simpson_result = labels[simpson_score.argmax()]

    return simpson_result


def main():
    label_binarizer = LabelBinarizer()

    matrix = np.array([['A', 'B', 'C', 'D'],
                       ['C', 'A', 'B', 'D'],
                       ['B', 'C', 'D', 'A'],
                       ['C', 'D', 'B', 'A'],])
    votes = np.array([5, 3, 6, 6])

    e = encoded(matrix, label_binarizer)

    labels = np.array(['A', 'B', 'C', 'D'])

    r = relative(labels, e, votes)
    print(r)
    a = absolute(labels, matrix, votes, e, label_binarizer)
    print(a)
    borda_res = borda(e, votes, labels)
    print(borda_res)
    condorse_res = condorse(matrix, votes, labels)
    print(condorse_res)
    kop_res = coplend(matrix, votes, labels)
    print(kop_res)
    simpson_res = simpson(matrix, votes, labels)
    print(simpson_res)


if __name__ == '__main__':
    main()
