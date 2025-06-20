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
from config import DEFAULT_BOARD_PATH, DEFAULT_LOOPS


def main():
    parser = parser_manager.init_parser()

    args = parser.parse_args()

    iterations = args_utils.get_k(args) or DEFAULT_LOOPS
    input_file = args_utils.get_input_file(args) or DEFAULT_BOARD_PATH
    output_file = args_utils.get_output_file(args)
    verbose = args_utils.is_verbose(args)


    if verbose:
        print("Wybrany plik: ", input_file)
        print("Wybrano algorytm:", args_utils.get_algorithm(args))

    controller = get_algorithm(args_utils.get_algorithm(args))
    if controller is None:
        print("Wybrano algorytm nie istnieje")
    if verbose:
        controller.print_name()

    board_str = board_file_util.read_board_flat(input_file or DEFAULT_BOARD_PATH)
    board_state = {}
    try:
        board_state = board_manager.create_board_from_string(board_str)
    except Exception as e:
        print(e)
        return
    if verbose:
        print('Rows: ', len(board_state['board_matrix']))
        print('Columns: ', len(board_state['board_matrix'][0]))
        print("Set board", end='\n\n')
        board_manager.print_board(board_state['board_matrix'])

    options = {}

    if args_utils.get_tabu_size(args):
        options['tabu_size'] = args_utils.get_tabu_size(args)
    if args_utils.get_start_temp(args):
        options['start_temp'] = args_utils.get_start_temp(args)
    if args_utils.get_alpha(args):
        options['alpha'] = args_utils.get_alpha(args)
    if args_utils.get_temp_function(args):
        options['temp_function'] = args_utils.get_temp_function(args)

    solution,iterations = controller.solve(board_state['board_matrix'], iterations, input_file, output_file, verbose, options)
    print("Solution:", end='\n')
    board_manager.print_board(solution)
    print("Iterations:", iterations, end='\n\n')
    print("Completeness: ", board_manager.calculate_board_completeness(solution))
if __name__ == "__main__":
    main()
