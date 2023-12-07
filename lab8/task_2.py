import numpy as np
from task_1 import nw_angle


def potential(supply_arr, demand_arr, cost_matrix):
    length_supply_arr = len(supply_arr)
    length_demand_arr = len(demand_arr)

    u = np.zeros(length_supply_arr)
    v = np.zeros(length_demand_arr)

    nw_result = nw_angle(np.copy(supply_arr), np.copy(demand_arr))

    modified_cost_matrix = np.copy(cost_matrix)

    for x in range(length_supply_arr + length_demand_arr - 1):
        for i in range(length_supply_arr):
            for j in range(length_demand_arr):
                if nw_result[i, j] > 0:
                    modified_cost_matrix[i,
                                         j] = cost_matrix[i, j] - u[i] - v[j]

        min_cost = np.min(modified_cost_matrix)
        min_indices = np.argwhere(modified_cost_matrix == min_cost)[0]

        u[min_indices[0]] += min_cost
        v[min_indices[1]] += min_cost

    result = nw_angle(np.copy(supply_arr), np.copy(demand_arr))

    return [result, u, v]


def main():
    supply_arr = np.array([200, 300, 250])
    demand_arr = np.array([210, 150, 120, 135, 135])
    cost_matrix = np.array([
        [20, 10, 13, 13, 18],
        [27, 19, 20, 16, 22],
        [26, 17, 19, 21, 23]
    ])

    potential_result = potential(
        supply_arr, demand_arr, cost_matrix)

    solution = potential_result[0]
    u = potential_result[1]
    v = potential_result[2]

    print(solution)
    print('u', u)
    print('v', v)


if __name__ == '__main__':
    main()
