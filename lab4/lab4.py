import numpy

def criterion_of_pessimism(paymatrix,alternatives):
    pessimism_results = [min(value) for value in paymatrix]

    best_result_pess = max(pessimism_results)
    best_index_pess = pessimism_results.index(max(pessimism_results))
    best_name_pess = alternatives[best_index_pess]

    print("Мінімальні значення:", pessimism_results)
    print(f"Найкраща альтернатива за критерієм песимізму (максимальне значення): {best_name_pess} - {best_result_pess}")

def criterion_of_optimism(paymatrix,alternatives):
    paymatrix_transp = paymatrix.transpose()
    max_in_col = [max(value) for value in paymatrix_transp]

    matrix_loses = [max_in_col - paymatrix]
    for i in range(0, len(matrix_loses)):
        print(matrix_loses[i])

    optimism_results = [max(value) for value in matrix_loses[0]]

    best_result_opt = min(optimism_results)
    best_index_opt = optimism_results.index(min(optimism_results))
    best_name_opt = alternatives[best_index_opt]

    print("Максимальні значення:", optimism_results)
    print(f"Найкраща альтернатива за критерієм оптимізму (мінімальне значення): {best_name_opt} - {best_result_opt}")

def Hurwitz_criterion(paymatrix,alternatives):
    gurvitz_results = [(optimism_indic * min(value) + (1 - optimism_indic) * max(value)) for value in paymatrix]

    best_result_gurvitz  = max(gurvitz_results)
    best_index_gurvitz = gurvitz_results.index(max(gurvitz_results))
    best_name_gurvitz= alternatives[best_index_gurvitz]

    print("Результат:", gurvitz_results)
    print(f"Найкраща альтернатива за критерієм Гурвіца (максимальне значення): {best_name_gurvitz} - {best_result_gurvitz}")

def Laplace_criterion(paymatrix,alternatives):
    laplas_results = [sum(values) / len(values) for values in paymatrix]

    best_result_laplas  = max(laplas_results)
    best_index_laplas = laplas_results.index(max(laplas_results))
    best_name_laplas = alternatives[best_index_laplas]

    print("Результат:", laplas_results)
    print(f"Найкраща альтернатива за критерієм Лапласа (максимальне значення): {best_name_laplas} - {best_result_laplas}")

def Bayes_Laplace_criterion(paymatrix,alternatives):
    bayes_laplas_results = [sum(value * probability for value, probability in zip(i, p)) for i in paymatrix]

    best_result_bayes_laplas  = max(bayes_laplas_results)
    best_index_bayes_laplas = bayes_laplas_results.index(max(bayes_laplas_results))
    best_name_bayes_laplas = alternatives[best_index_bayes_laplas]

    print("Результат:", bayes_laplas_results)
    print(f"Найкраща альтернатива за критерієм Байєса-Лапласа (максимальне значення): {best_name_bayes_laplas} - {best_result_bayes_laplas}")

def Hodge_Liman_criterion(paymatrix,alternatives):
    khoj_lehman_results = [sum(value * probability for value, probability in zip(i, p)) for i in paymatrix]

    target_functions = [optimism_indic * expected_effect + (1 - optimism_indic) * max(value) for expected_effect, value in zip(khoj_lehman_results, paymatrix)]

    best_result_khoj_lehman  = max(target_functions)
    best_index_khoj_lehman = target_functions.index(max(target_functions))
    best_name_khoj_lehman = alternatives[best_index_khoj_lehman]

    print("Результат:", target_functions)
    print(f"Найкраща альтернатива за Критерієм Ходжа-Лемана (максимальне значення) (λ = {optimism_indic}): {best_name_khoj_lehman} - {best_result_khoj_lehman}")

k = 2

if k >= 1 | k <= 12: 
    optimism_indic = 1 / (k + 3)
else:
    optimism_indic = 4 / k

paymatrix = numpy.array([
    [180, 140, k, (245-4*k), 232],
    [420, (120+10*k), 140, 220, 100],
    [(25+8*k), 315, 35, 49, (10*(k+23)-50)],
    [(290-10*k), k, 9, (100*k-90), 201]
])

alternatives = ['A1', 'A2', 'A3', 'A4']

p = [0.1, 0.2, optimism_indic, optimism_indic + 0.1, 0.6 - 2 * optimism_indic]

print("Матриця платежів:")
for i in range(0, len(paymatrix)):
    print(paymatrix[i])


criterion_of_pessimism(paymatrix,alternatives)

criterion_of_optimism(paymatrix,alternatives)

Hurwitz_criterion(paymatrix,alternatives)

Laplace_criterion(paymatrix,alternatives)

Bayes_Laplace_criterion(paymatrix,alternatives)

Hodge_Liman_criterion(paymatrix,alternatives)