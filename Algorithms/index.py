import Algorithms.HillClimb.index as hc
import Algorithms.Tabu.index as tabu
import Algorithms.HillClimbStochastic.index as hs

def get_algorithm(name):
    if name == "hill_climb":
        return hc
    elif name == "hill_climb_stochastic":
        return hs
    elif name == "tabu":
        return tabu
    else:
        return None