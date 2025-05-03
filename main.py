# This is the main file to use all the algorithms.
#external imports
import argparse
import importlib

#interanl imports
import Utils.args_utils as args_utils
import Managers.parser_manager as parser_manager
from Algorithms.index import get_algorithm
import Utils.board_file_util as board_file_util
import Managers.board_manager as board_manager
from config import DEFAULT_BOARD_PATH


def main():
    parser = parser_manager.init_parser()

    args = parser.parse_args()

    if args_utils.is_verbose(args):
        print("Wybrano algorytm:", args_utils.get_algorithm(args))

    controller = get_algorithm(args_utils.get_algorithm(args))
    if controller is None:
        print("Wybrano algorytm nie istnieje")
    controller.test()

    board_str = board_file_util.read_board_flat(DEFAULT_BOARD_PATH)
    board_manager.set_board(board_str)
    print("Set board", end='\n')
    board_manager.print_board()
    board_manager.place(1,0)
    print("Placed light", end='\n')
    board_manager.print_board()

if __name__ == "__main__":
    main()
