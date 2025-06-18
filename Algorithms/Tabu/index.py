import copy
from random import randint

import Managers.algorithms_manager as am

def print_name():
    print("Test Tabu")
    return

def solve(initial_board_matrix, k, input_path, output_path, verbose, options=None):
    if options is None:
        options = {
            "tabu_size": 100, #set to -1 for unlimited tabu
            "use_history": True
        }
    tabu_size = options["tabu_size"]
    current = am.random_solution(initial_board_matrix)
    global_best = [copy.copy(current)]
    tabu_list = [copy.copy(current)]
    history_list = [copy.copy(current)]

    for i in range(k):
        neighbours = [n for n in am.generate_neighbours(current) if n not in tabu_list]
        if options["use_history"]:
            while len(neighbours) == 0 and len(history_list) > 0:
                current = history_list.pop()
                neighbours = [n for n in am.generate_neighbours(current) if n not in tabu_list]

        if len(neighbours) == 0: break
        best_neighbour = neighbours[0]
        for j in neighbours[1:]:
            if am.loss(j) < am.loss(best_neighbour):
                best_neighbour = j
        if options["use_history"]:
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
    return global_best[-1], k