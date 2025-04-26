from argparse import Namespace


def get_algorithm(args: Namespace):
    return args.algorithm

def is_verbose(args: Namespace):
    return args.verbose

def get_k(args: Namespace):
    return args.k

def get_input_file(args: Namespace):
    return args.input_file

def get_output_file(args: Namespace):
    return args.output_file