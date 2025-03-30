# This is the main file to use all the algorithms.
#external imports
import argparse

#interanl imports
import Utils.args_utils as args_utils
import Managers.parser_manager as parser_manager

def main():
    parser = parser_manager.init_parser()

    args = parser.parse_args()

    if args_utils.is_verbose(args):
        print("Wybrano algorytm:", args_utils.get_algorithm(args))

if __name__ == "__main__":
    main()
