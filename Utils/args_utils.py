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

def get_tabu_size(args: Namespace):
    return args.tabu_size

def get_alpha(args: Namespace):
    return args.alpha

def get_temp_function(args: Namespace):
    return args.temp_function

def get_start_temp(args: Namespace):
    return args.start_temp