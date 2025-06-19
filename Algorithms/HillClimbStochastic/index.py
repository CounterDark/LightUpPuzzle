from random import randint

import Managers.algorithms_manager as am

def print_name():
    print("Test Hill Climb Stochastic")
    return

def solve(initial_board_matrix, k, input_path, output_path, verbose, options=None):
    current = am.random_solution(initial_board_matrix)
    for i in range(k):
        neighbours = am.generate_neighbours(current)
        neighbour = neighbours[randint(0,len(neighbours)-1)]
        if am.loss(neighbour) <= am.loss(current):
                current = neighbour
        if am.loss(current) == 0:
            return current, i
        if verbose:
            print("Iteration Completeness: ", 1.0 - am.loss(current))
    return current, k