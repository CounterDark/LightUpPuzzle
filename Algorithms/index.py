import Algorithms.HillClimb.index as hc
import Algorithms.Tabu.index as tabu
import Algorithms.HillClimbStochastic.index as hs
import Algorithms.BruteForce.index as br

def get_algorithm(name):
    if name == "hill_climb":
        return hc
    elif name == "hill_climb_stochastic":
        return hs
    elif name == "tabu":
        return tabu
    elif name == "brute_force":
        return br
    else:
        return None