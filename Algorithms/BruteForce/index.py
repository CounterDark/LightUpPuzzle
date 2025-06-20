import copy
from random import randint, choice

import Managers.algorithms_manager as am

def print_name():
    print("Test Brute Force")
    return

# Optimized brute force with stop on complete
def solve(initial_board_matrix, k, input_path, output_path, verbose, options=None):
    global_best = [initial_board_matrix]
    best_loss = am.loss(initial_board_matrix)
    options = options or {}
    stop_on_completeness = options.get('stop_on_completeness', True)

    iterations = 0

    if verbose:
        print("Brute Force started.")

    global_paths = am.generate_neighbours(initial_board_matrix, only_place=True)
    while iterations < k and len(global_paths) > 0:
        # if verbose:
        #     print("Iteration #", iterations)
        #     print("Best loss:", best_loss)
        #     print("Paths amount:", len(global_paths))
        current_path = global_paths.pop(0)
        loss = am.loss(current_path)
        # if verbose:
        #     print("Current loss:", loss)
        if loss == 0.0:
            if stop_on_completeness:
                return current_path, iterations
            if best_loss > 0.0:
                best_loss = 0.0
                global_best.clear()
            if verbose:
                print("Found solution at iteration ", iterations)
            global_best.append(current_path)
        else:
            if best_loss > loss:
                global_best.clear()
                best_loss = loss
                global_best.append(current_path)
                if verbose:
                    print("Best loss: ", best_loss)
            path_neighbours = am.generate_neighbours(current_path, only_place=True)
            global_paths.extend(path_neighbours)
        if verbose:
            print("Iteration Completeness: ", 1.0 - best_loss)
        iterations += 1
    if verbose:
        print("Global best paths: ", len(global_best))
    random_best = choice(global_best)
    return random_best, iterations

# Field by field brute force
# def solve(initial_board_matrix, k, input_path, output_path, verbose, options=None):
#     global_best = [initial_board_matrix]
#     best_completeness = 1.0 - am.loss(initial_board_matrix)
#     options = options or {
#         "stop_on_complete": True
#     }
#
#     iterations = 0
#
#     if verbose:
#         print("Brute Force started.")
#
#     fields = am.generate_neighbours(initial_board_matrix, only_place=True)
#     if verbose:
#         print("Fields: ", len(fields))
#     for field in fields:
#         if iterations >= k:
#             break
#         if verbose:
#             print("Starting field")
#             print("Starting iteration: ", iterations)
#         next_paths = am.generate_neighbours(field, only_place=True)
#         current_paths = copy.copy(next_paths)
#         while len(current_paths) > 0 and iterations < k:
#             current_paths = copy.copy(next_paths)
#             if verbose:
#                 print("Iteration: ", iterations)
#                 print("Current paths: ", len(current_paths))
#             next_paths.clear()
#             for path in current_paths:
#                 if am.loss(path) == 0.0:
#                     if best_completeness < 1.0:
#                         best_completeness = 1.0
#                         global_best.clear()
#                     global_best.append(path)
#                 else:
#                     path_neighbours = am.generate_neighbours(path, only_place=True)
#                     if len(path_neighbours) == 0 and best_completeness < (1.0 - am.loss(path)):
#                         global_best.clear()
#                         best_completeness = 1.0-am.loss(path)
#                         global_best.append(path)
#                     else:
#                         next_paths.extend(path_neighbours)
#             iterations += 1
#     random_best = choice(global_best)
#     return random_best, iterations

# Basic brute, very long time
# def solve(initial_board_matrix, k, input_path, output_path, verbose, options=None):
#     global_best = []
#     best_completness = 0
#
#     iterations = 0
#
#     print("Brute Force started.")
#
#     next_paths = am.generate_neighbours(initial_board_matrix, only_place=True)
#     while iterations < k and len(next_paths) > 0:
#         current_paths = copy.copy(next_paths)
#         next_paths.clear()
#         print("Iteration: ", iterations)
#         print("Current paths: ", len(current_paths))
#         local_i = 0
#         for path in current_paths:
#             local_i += 1
#             print("Starting path: ", local_i)
#             if am.loss(path) == 0:
#                 if best_completness < (1-am.loss(path)):
#                     best_completness = 1-am.loss(path)
#                     global_best.clear()
#                 global_best.append(path)
#             else:
#                 path_neighbours = am.generate_neighbours(path, only_place=True)
#                 if len(path_neighbours) == 0 and best_completness < (1-am.loss(path)):
#                     global_best.clear()
#                     global_best.append(path)
#                 else:
#                     next_paths.extend(path_neighbours)
#             iterations += 1
#     random_best = choice(global_best)
#     return random_best, iterations



# def solve_paths(paths, limit, curr_path_iterations, verbose, options=None):
#     local_iterations = curr_path_iterations
#     best_paths = []
#     best_iteration = local_iterations
#     best_completeness = 0.0
#     for path in paths:
#          local_iterations += 1
#          if local_iterations > limit:
#              break
#          completeness = 1 - am.loss(path)
#          if completeness == 100 and best_iteration < local_iterations:
#              best_paths.append(path)
#              best_iteration = local_iterations
#              best_completeness = 100.0
#
#          next_paths = am.generate_neighbours(path, True)
#          paths_count = len(next_paths)
#          if paths_count == 0 and best_iteration < local_iterations and best_completeness < completeness:
#              best_paths = path
#              best_iteration = local_iterations
#              best_completeness = completeness
#          else:
#             result_bests, result_iterations, result_completness = solve(next_paths, limit, local_iterations, verbose, options)
#             if result_iterations >= best_iteration and result_completness >= best_completeness:
#                 best_paths.append
#     return best_paths, best_iteration, best_completeness