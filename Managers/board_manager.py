from typing import TypedDict, List
import random

class BoardState(TypedDict):
    rows: int
    columns: int
    board_matrix: List[List[str]]
    start_board_string: str
    current_board_string: str

class Coordinate(TypedDict):
    x: int
    y: int

class Action(TypedDict):
    action: str
    coordinate: Coordinate

def create_board_from_string(board_string, start_string = '') -> BoardState:
    start_board_string = ''
    if start_string == '':
        start_board_string = board_string.strip()
    current_board_string = board_string
    rows_data = current_board_string.split(',')
    rows = len(rows_data)
    board_matrix = [row.split('.') for row in rows_data]
    columns = len(board_matrix[0]) if rows > 0 else 0
    for row in board_matrix:
        if len(row) != columns:
            raise Exception('Invalid row size')
    return {
        'rows': rows,
        'columns': columns,
        'board_matrix': board_matrix,
        'start_board_string': start_board_string,
        'current_board_string': current_board_string,
    }

def get_field(x, y, board_matrix) -> str:
    rows = len(board_matrix)
    columns = len(board_matrix[0])
    if x < 0 or x >= columns or y < 0 or y >= rows:
        raise IndexError
    return board_matrix[y][x]

def safe_get_field(x, y, board_matrix) -> str:
    rows = len(board_matrix)
    columns = len(board_matrix[0])
    if x < 0 or x >= columns or y < 0 or y >= rows:
        return ''
    return get_field(x, y, board_matrix)

def set_field(x, y, value, board_matrix):
    rows = len(board_matrix)
    columns = len(board_matrix[0])
    if x < 0 or x >= columns or y < 0 or y >= rows:
        raise Exception('Invalid coordinate')
    if (value == '1') and (not board_matrix[y][x].startswith('b')) and (not board_matrix[y][x].startswith('l')):
        board_matrix[y][x] = str(int(board_matrix[y][x]) + 1)
    elif (value == '0') and (not board_matrix[y][x].startswith('b')) and (not board_matrix[y][x].startswith('l')):
        board_matrix[y][x] = str(max(int(board_matrix[y][x]) - 1, 0))
    else:
        board_matrix[y][x] = value


def place(x, y, board_matrix):
    rows = len(board_matrix)
    columns = len(board_matrix[0])
    if x < 0 or x >= columns or y < 0 or y >= rows:
        raise Exception('Invalid coordinate')
    left_incomplete = True
    right_incomplete = True
    top_incomplete = True
    bottom_incomplete = True
    board_matrix[y][x] = 'l'
    x_offset = 1
    y_offset = 1
    iteration = 0
    while left_incomplete or right_incomplete or top_incomplete or bottom_incomplete:
        if bottom_incomplete and (y + y_offset < rows):
            field = get_field(x, y + y_offset, board_matrix)
            if field == '':
                bottom_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in column')
            elif field.startswith('b'):
                bottom_incomplete = False
            else:
                set_field(x, y + y_offset, '1', board_matrix)
        elif bottom_incomplete:
            bottom_incomplete = False

        if top_incomplete and (y - y_offset >= 0):
            field = get_field(x, y - y_offset, board_matrix)
            if field == '':
                top_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in column')
            elif field.startswith('b'):
                top_incomplete = False
            else:
                set_field(x, y - y_offset, '1', board_matrix)
        elif top_incomplete:
            top_incomplete = False

        if left_incomplete and (x - x_offset >= 0):
            field = get_field(x - x_offset, y, board_matrix)
            if field == '':
                left_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in row')
            elif field.startswith('b'):
                left_incomplete = False
            else:
                set_field(x - x_offset, y, '1', board_matrix)
        elif left_incomplete:
            left_incomplete = False

        if right_incomplete and (x + x_offset < columns):
            field = get_field(x + x_offset, y, board_matrix)
            if field == '':
                right_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in row')
            elif field.startswith('b'):
                right_incomplete = False
            else:
                set_field(x + x_offset, y, '1', board_matrix)
        elif right_incomplete:
            right_incomplete = False

        x_offset = x_offset + 1
        y_offset = y_offset + 1
        iteration += 1
    return board_matrix

def remove(x, y, board_matrix):
    rows = len(board_matrix)
    columns = len(board_matrix[0])
    if x < 0 or x >= columns or y < 0 or y >= rows:
        raise Exception('Invalid coordinate')
    left_incomplete = True
    right_incomplete = True
    top_incomplete = True
    bottom_incomplete = True
    board_matrix[y][x] = '0'
    x_offset = 1
    y_offset = 1
    iteration = 0
    while (iteration < 10) and (left_incomplete or right_incomplete or top_incomplete or bottom_incomplete):
        if bottom_incomplete and (y + y_offset < rows):
            field = get_field(x, y + y_offset, board_matrix)
            if field == '':
                bottom_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in column')
            elif field.startswith('b'):
                bottom_incomplete = False
            else:
                set_field(x, y + y_offset, '0', board_matrix)
        elif bottom_incomplete:
            bottom_incomplete = False

        if top_incomplete and (y - y_offset >= 0):
            field = get_field(x, y - y_offset, board_matrix)
            if field == '':
                top_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in column')
            elif field.startswith('b'):
                top_incomplete = False
            else:
                set_field(x, y - y_offset, '0', board_matrix)
        elif top_incomplete:
            top_incomplete = False

        if left_incomplete and (x - x_offset >= 0):
            field = get_field(x - x_offset, y, board_matrix)
            if field == '':
                left_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in row')
            elif field.startswith('b'):
                left_incomplete = False
            else:
                set_field(x - x_offset, y, '0', board_matrix)
        elif left_incomplete:
            left_incomplete = False

        if right_incomplete and (x + x_offset < columns):
            field = get_field(x + x_offset, y, board_matrix)
            if field == '':
                right_incomplete = False
            elif field == 'l':
                raise Exception('lamp already placed in row')
            elif field.startswith('b'):
                right_incomplete = False
            else:
                set_field(x + x_offset, y, '0', board_matrix)
        elif right_incomplete:
            right_incomplete = False

        x_offset = x_offset + 1
        y_offset = y_offset + 1
        iteration += 1
    return board_matrix

def parse_board_matrix(board_matrix) -> str:
    return ','.join('.'.join(row) for row in board_matrix)


def print_board(board_matrix):
    for row in board_matrix:
        print('.'.join(row))

# TODO: Fix the priority coordinates later
# def get_available_coordinates_with_priority(board_matrix) -> List[Coordinate]:
#     available_coordinates = []
#     for row_index, row in enumerate(board_matrix):
#         for col_index, column in enumerate(row):
#             if column.startswith('l'):
#                 continue
#             elif column.startswith('b'):
#                 if column == 'b':
#                     continue
#                 else:
#                     required_lights = int(column[1:])
#                     if required_lights > 0:
#                         for i in range(required_lights):
#                             available_coordinates.append({'x': col_index, 'y': row_index})
#             elif column != '0':
#                 continue
#             else:
#                 if check_adjacent_coordinates(col_index, row_index, board_matrix):
#                     available_coordinates.append({'x': col_index, 'y': row_index})
#     return available_coordinates

# Available coordinates are actually neighbours
def get_available_coordinates(board_matrix) -> List[Coordinate]:
    available_coordinates = []
    for row_index, row in enumerate(board_matrix):
        for col_index, column in enumerate(row):
            if column.startswith('l'):
                continue
            elif column.startswith('b'):
                continue
            elif column != '0':
                continue
            else:
                available_coordinates.append({'x': col_index, 'y': row_index})
    return available_coordinates

def get_remove_candidates(board_matrix) -> List[Coordinate]:
    remove_candidates = []
    for y, row in enumerate(board_matrix):
        for x, column in enumerate(row):
            if column.startswith('l'):
                remove_candidates.append({'x': x, 'y': y})
    return remove_candidates

def get_actions(board_matrix) -> List[Action]:
    actions = []
    for row_index, row in enumerate(board_matrix):
        for col_index, column in enumerate(row):
            if column.startswith('l'):
                actions.append(Action(action='r', coordinate={'x': col_index, 'y': row_index}))
                continue
            elif column.startswith('b'):
                continue
            elif column != '0':
                continue
            else:
                actions.append(Action(action='p', coordinate={'x': col_index, 'y': row_index}))
    return actions

def check_adjacent_coordinates(x, y, board_matrix) -> bool:
    up_field = safe_get_field(x, y - 1, board_matrix)
    down_field = safe_get_field(x, y + 1, board_matrix)
    left_field = safe_get_field(x - 1, y, board_matrix)
    right_field = safe_get_field(x + 1, y, board_matrix)
    if up_field == 'b0':
        return False
    if down_field == 'b0':
        return False
    if left_field == 'b0':
        return False
    if right_field == 'b0':
        return False
    return True

def get_fill_amount(board_matrix) -> float:
    filled_fields = 0
    total = 0
    for y, row in enumerate(board_matrix):
        for x, column in enumerate(row):
            if column.startswith('b'):
                continue
            if column.startswith('l') or column != '0':
                filled_fields += 1
            total += 1
    if total == 0:
        return 0.0
    return filled_fields / total

def get_required_fill_amount(board_matrix) -> float:
    required_fill_amount = 0.0
    total = 0
    for y, row in enumerate(board_matrix):
        for x, column in enumerate(row):
            if column.startswith('l'):
                if not check_adjacent_coordinates(x, y, board_matrix):
                    required_fill_amount -= 1
                    total += 1
            if column.startswith('b') and (len(column) == 2):
                value = int(column[1])
                if value == 0:
                    continue
                field_fill = calculate_required_field_value(value, x, y, board_matrix)
                required_fill_amount += field_fill
                total += 1
    if total == 0:
        return 0.0
    return max(required_fill_amount, 0) / total



def calculate_required_field_value(value, x, y, board_matrix) -> float:
    if value == 0:
        return 0.0
    total = 0
    up_field = safe_get_field(x, y - 1, board_matrix)
    down_field = safe_get_field(x, y + 1, board_matrix)
    left_field = safe_get_field(x - 1, y, board_matrix)
    right_field = safe_get_field(x + 1, y, board_matrix)
    if (not up_field.startswith('b')) and up_field.startswith('l'):
        total += 1
    if (not down_field.startswith('b')) and down_field.startswith('l'):
        total += 1
    if (not left_field.startswith('b')) and left_field.startswith('l'):
        total += 1
    if (not right_field.startswith('b')) and right_field.startswith('l'):
        total += 1
    return (min(total, value) - (max(total, value)-value)) / value

# board completeness is a way to measure loss value
def calculate_board_completeness(board_matrix) -> float:
    # return get_fill_amount(board_matrix) * get_required_fill_amount(board_matrix)
    required_fill_amount = 0.0
    total_required = 0
    filled_fields = 0
    total_fill_fields = 0
    for y, row in enumerate(board_matrix):
        for x, column in enumerate(row):
            if column.startswith('l'):
                if not check_adjacent_coordinates(x, y, board_matrix):
                    required_fill_amount -= 1
                    total_required += 1
                filled_fields += 1
            elif column.startswith('b') and (len(column) == 2):
                value = int(column[1])
                if value == 0:
                    continue
                field_fill = calculate_required_field_value(value, x, y, board_matrix)
                required_fill_amount += field_fill
                total_required += 1
                continue
            elif column.startswith('b'):
                continue
            elif column != '0':
                filled_fields += 1
            total_fill_fields += 1
    if total_required == 0 or total_fill_fields == 0:
        return 0.0
    return (filled_fields / total_fill_fields) * (max(required_fill_amount, 0) / total_required)
    # return get_fill_amount(board_matrix)

def random_fill_board(board_matrix, force_limit = 20):
    is_complete = False
    iteration = 0
    while (iteration<=force_limit) and (not is_complete):
        iteration += 1
        choices = get_actions(board_matrix)
        if len(choices) == 0:
            is_complete = True
            break
        action = random.choice(choices)
        # print('Action:', action, end='\n')
        if action['action'] == 'p':
            place(action['coordinate']['x'], action['coordinate']['y'], board_matrix)
        elif action['action'] == 'r':
            remove(action['coordinate']['x'], action['coordinate']['y'], board_matrix)
        completeness = calculate_board_completeness(board_matrix)
        # print('Completeness:', completeness)
        if completeness == 1.0:
            # print('Iterations: ', iteration)
            is_complete = True
    return board_matrix