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
    board_state = board_manager.create_board_from_string(board_str)
    print('Rows: ', len(board_state['board_matrix']))
    print('Columns: ', len(board_state['board_matrix'][0]))
    print("Set board", end='\n\n')
    board_manager.print_board(board_state['board_matrix'])
    print("Board completeness", end='\n')
    print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(1, 0, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(4, 0, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(3, 1, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(0, 2, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(2, 2, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(9, 2, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(1, 3, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(6, 4, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(3, 5, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(7, 5, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(2, 6, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(5, 6, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(8, 6, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(0, 7, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(4, 7, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(9, 7, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(8, 8, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(2, 9, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    # board_manager.place(7, 9, board_state['board_matrix'])
    # print("Board completeness", end='\n')
    # print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    board_manager.random_fill_board(board_state['board_matrix'])
    print(board_manager.calculate_board_completeness(board_state['board_matrix']))
    board_manager.print_board(board_state['board_matrix'])

if __name__ == "__main__":
    main()
