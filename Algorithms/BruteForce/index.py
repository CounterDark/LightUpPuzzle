import copy
from random import randint

import Managers.algorithms_manager as am

def print_name():
    print("Test Brute Force")
    return

def solve(initial_board_matrix, k, input_path, output_path, verbose, options=None):
    global_best = []
    best_iteration = 0
    paths_count = 0
    stop_all = False

    iterations = 0

    main_paths = am.generate_neighbours(initial_board_matrix)
    paths_count = len(main_paths)



def solve_paths(paths, limit, curr_path_iterations, verbose, options=None):
    local_iterations = curr_path_iterations
    best_paths = []
    best_iteration = local_iterations
    best_completeness = 0.0
    for path in paths:
         local_iterations += 1
         if local_iterations > limit:
             break
         completeness = 1 - am.loss(path)
         if completeness == 100 and best_iteration < local_iterations:
             best_paths.append(path)
             best_iteration = local_iterations
             best_completeness = 100.0

         next_paths = am.generate_neighbours(path, True)
         paths_count = len(next_paths)
         if paths_count == 0 and best_iteration < local_iterations and best_completeness < completeness:
             best_paths = path
             best_iteration = local_iterations
             best_completeness = completeness
         else:
            result_bests, result_iterations, result_completness = solve(next_paths, limit, local_iterations, verbose, options)
            if result_iterations >= best_iteration and result_completness >= best_completeness:
                best_paths.append
    return best_paths, best_iteration, best_completeness