import copy
from random import randint

import Managers.algorithms_manager as am

def print_name():
    print("Test Tabu")
    return

def solve(initial_board_matrix, k, input_path, output_path, verbose, options=None):
    options = options or {}
    tabu_size = options.get('tabu_size', 100)
    use_history = options.get('use_history', True)

    current = am.random_solution(initial_board_matrix)
    global_best = [copy.copy(current)]
    tabu_list = [copy.copy(current)]
    history_list = [copy.copy(current)]

    for i in range(k):
        neighbours = [n for n in am.generate_neighbours(current) if n not in tabu_list]
        if use_history:
            while len(neighbours) == 0 and len(history_list) > 0:
                current = history_list.pop()
                neighbours = [n for n in am.generate_neighbours(current) if n not in tabu_list]

        if len(neighbours) == 0: break
        best_neighbour = neighbours[0]
        for j in neighbours[1:]:
            if am.loss(j) < am.loss(best_neighbour):
                best_neighbour = j
        if use_history:
            history_list.append(current)
        current = best_neighbour
        tabu_list.append(best_neighbour)
        if tabu_size < 0 or len(tabu_list) > tabu_size:
            tabu_list = tabu_list[-tabu_size:]
        loss = am.loss(current)
        if loss < am.loss(global_best[-1]):
            if verbose:
                print("Found better solution on iteration ", i)
                print("Current loss: ", loss)
            global_best.append(current)
        if loss == 0:
            return current, i
        if verbose:
            print("Iteration Completeness: ", 1.0 - am.loss(global_best[-1]))
    return global_best[-1], k