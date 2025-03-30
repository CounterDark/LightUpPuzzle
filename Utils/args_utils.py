from argparse import Namespace


def get_algorithm(args: Namespace):
    return args.algorithm

def is_verbose(args: Namespace):
    return args.verbose