from config import DEFAULT_INPUT_DIR, DEFAULT_OUTPUT_DIR, DEFAULT_LOOPS
import Managers.algorithms_manager as am

def print_name():
    print("Test Hill Climb")
    return

def solve(initial_board_matrix, k, input_path, output_path, verbose):
    current = am.random_solution(initial_board_matrix)
    for i in range(k):
        neighbours = am.generate_neighbours(current)
        best_neighbour = neighbours[0]
        for j in neighbours[1:]:
            if am.loss(j) < am.loss(best_neighbour):
                best_neighbour = j
        if am.loss(best_neighbour) < am.loss(current):
            current = best_neighbour
        else:
            return current, i
    return current, k