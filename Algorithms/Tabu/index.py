import copy
from random import randint

import Managers.algorithms_manager as am

def print_name():
    print("Test Tabu")
    return

def solve(initial_board_matrix, k, input_path, output_path, verbose, options=None):
    if options is None:
        options = {
            "tabu_size": 100,
        }
    tabu_size = options["tabu_size"]
    current = am.random_solution(initial_board_matrix)
    global_best = [copy.copy(current)]
    tabu_list = [copy.copy(current)]

    for i in range(k):
        neighbours = [n for n in am.generate_neighbours(current) if n not in tabu_list]
        if len(neighbours) == 0: break
        best_neighbour = neighbours[0]
        for j in neighbours[1:]:
            if am.loss(j) < am.loss(best_neighbour):
                best_neighbour = j
        current = best_neighbour
        tabu_list.append(best_neighbour)
        if len(tabu_list) > tabu_size:
            tabu_list = tabu_list[-tabu_size:]
        if am.loss(current) < am.loss(global_best[-1]):
            global_best.append(current)
        if am.loss(current) == 0:
            return current, i
        if verbose:
            print('tabu: ', len(tabu_list))
    return global_best[-1], k