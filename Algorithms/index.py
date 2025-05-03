import Algorithms.HillClimb.index as hc
import Algorithms.Tabu.index as tabu

def get_algorithm(name):
    if name == "hill_climb":
        return hc
    elif name == "tabu":
        return tabu
    else:
        return None