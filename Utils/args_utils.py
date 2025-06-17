from argparse import Namespace
from config import DEFAULT_LOOPS, DEFAULT_INPUT_DIR, DEFAULT_OUTPUT_DIR


def get_algorithm(args: Namespace):
    return args.algorithm

def is_verbose(args: Namespace):
    return args.verbose or False

def get_k(args: Namespace):
    return args.k

def get_input_file(args: Namespace):
    return args.input_file

def get_output_file(args: Namespace):
    return args.output_file