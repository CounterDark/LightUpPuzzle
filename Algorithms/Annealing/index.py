import math
import random
import copy
import Managers.algorithms_manager as am

def print_name():
    print("Simulated Annealing")
    return

MIN_TEMPERATURE = 0.000001

def temperature_linear(t, alpha):
    return max(t - alpha, MIN_TEMPERATURE)

def temperature_exponential(t, alpha):
    return max(t * math.exp(-alpha), MIN_TEMPERATURE)

def temperature_logarithmic(t, i):
    return max(t / math.log(i + 2), MIN_TEMPERATURE)

def select_neighbour(neighbours):
    if not neighbours:
        return None
    index = int(random.gauss(len(neighbours) // 2, len(neighbours) / 5))
    index = max(0, min(index, len(neighbours) - 1))
    return neighbours[index]

def solve(initial_board_matrix, k, input_path, output_path, verbose, options=None):
    options = options or {}

    t = options.get("t0", 1.0)
    alpha = options.get("alpha", 0.01)
    temp_func = options.get("temp_function", "linear")

    if temp_func == "exponential":
        temp = lambda temperature, iteration: temperature_exponential(temperature, alpha)
    elif temp_func == "log":
        temp = lambda temperature, iteration: temperature_logarithmic(temperature, iteration)
    else:
        temp = lambda temperature, iteration: temperature_linear(temperature, alpha)

    current = am.random_solution(initial_board_matrix)
    current_loss = am.loss(current)

    if verbose:
        print("Starting Annealing")

    for i in range(k):
        neighbours = am.generate_neighbours(current)
        neighbour = select_neighbour(neighbours)
        if neighbour is None:
            break
        neighbour_loss = am.loss(neighbour)

        delta = neighbour_loss - current_loss

        if delta < 0 or random.random() < math.exp(-delta / t):
            current = neighbour
            current_loss = neighbour_loss

        if current_loss == 0.0:
            return current, i

        t = temp(t, i)
        if verbose:
            print("Iteration Completeness: ", 1.0 - current_loss)

    return current, k