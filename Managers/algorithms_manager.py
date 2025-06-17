import copy
import Managers.board_manager as board_manager

def loss(board_matrix):
    return 1.0 - board_manager.calculate_board_completeness(board_matrix)

def random_solution(board_matrix):
    return board_manager.random_fill_board(board_matrix)

def generate_neighbours(board_matrix, only_place=False):
    actions = board_manager.get_actions(board_matrix)
    neighbours = []
    for action in actions:
        copy_board = copy.deepcopy(board_matrix)
        if action["action"] == 'p':
            neighbours.append(board_manager.place(action["coordinate"]["x"], action["coordinate"]["y"], copy_board))
        elif not only_place and action["action"] == 'r':
            neighbours.append(board_manager.remove(action["coordinate"]["x"], action["coordinate"]["y"], copy_board))
    return neighbours
