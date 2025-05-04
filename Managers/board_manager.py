from typing import TypedDict, List

class BoardState(TypedDict):
    rows: int
    columns: int
    board_matrix: List[List[str]]
    start_board_string: str
    current_board_string: str


def create_board_from_string(board_string, start_string = '') -> BoardState:
    start_board_string = ''
    if start_string == '':
        start_board_string = board_string.strip()
    current_board_string = board_string
    rows_data = current_board_string.split(',')
    rows = len(rows_data)
    board_matrix = [row.split('.') for row in rows_data]
    columns = len(board_matrix[0]) if rows > 0 else 0
    return {
        'rows': rows,
        'columns': columns,
        'board_matrix': board_matrix,
        'start_board_string': start_board_string,
        'current_board_string': current_board_string,
    }

def get_field(x, y, board_matrix, columns, rows) -> str:
    if x < 0 or x >= columns or y < 0 or y >= rows:
        raise IndexError
    return board_matrix[y][x]

def set_field(x, y, value, board_matrix, columns, rows):
    if x < 0 or x >= columns or y < 0 or y >= rows:
        raise Exception('Invalid coordinate')
    board_matrix[y][x] = value


def place(x, y, board_matrix, columns, rows):
    if x < 0 or x >= columns or y < 0 or y >= rows:
        raise Exception('Invalid coordinate')
    left_incomplete = True
    right_incomplete = True
    top_incomplete = True
    bottom_incomplete = True
    board_matrix[y][x] = 'l'
    x_offset = 1
    y_offset = 1
    while left_incomplete or right_incomplete or top_incomplete or bottom_incomplete:
        if y + y_offset >= rows:
            bottom_incomplete = False
        else:
            field = get_field(x, y + y_offset, board_matrix, columns, rows)
            if field == '':
                bottom_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in column')
            elif field.startswith('b'):
                bottom_incomplete = False
            else:
                set_field(x, y + y_offset, '1', board_matrix, columns, rows)

        if y - y_offset < 0:
            top_incomplete = False
        else:
            field = get_field(x, y - y_offset, board_matrix, columns, rows)
            if field == '':
                top_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in column')
            elif field.startswith('b'):
                top_incomplete = False
            else:
                set_field(x, y - y_offset, '1', board_matrix, columns, rows)

        if x - x_offset < 0:
            left_incomplete = False
        else:
            field = get_field(x - x_offset, y, board_matrix, columns, rows)
            if field == '':
                left_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in column')
            elif field.startswith('b'):
                left_incomplete = False
            else:
                set_field(x - x_offset, y, '1', board_matrix, columns, rows)

        if x + x_offset < 0:
            right_incomplete = False
        else:
            field = get_field(x + x_offset, y, board_matrix, columns, rows)
            if field == '':
                right_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in column')
            elif field.startswith('b'):
                right_incomplete = False
            else:
                set_field(x + x_offset, y, '1', board_matrix, columns, rows)

        x_offset = x_offset + 1
        y_offset = y_offset + 1
    return board_matrix

def parse_board_matrix(board_matrix) -> str:
    return ','.join('.'.join(row) for row in board_matrix)


def print_board(board_matrix):
    for row in board_matrix:
        print('.'.join(row))