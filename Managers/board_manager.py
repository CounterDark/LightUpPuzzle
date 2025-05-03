start_board_string = ''
rows = 0
columns = 0
board_matrix = []

def set_board(board_string):
    global start_board_string
    global rows
    global columns
    global board_matrix
    start_board_string = board_string.strip()
    rows_data = start_board_string.split(',')
    rows = len(rows_data)
    board_matrix = [row.split('.') for row in rows_data]
    columns = len(board_matrix[0]) if rows > 0 else 0

def get_field(x, y) -> str:
    global start_board_string
    global rows
    global columns
    global board_matrix
    if x < 0 or x >= columns or y < 0 or y >= rows:
        return ''
    return board_matrix[y][x]

def set_field(x, y, value):
    global start_board_string
    global rows
    global columns
    global board_matrix
    if x < 0 or x >= columns or y < 0 or y >= rows:
        Exception('Invalid coordinate')
        return
    board_matrix[y][x] = value


def place(x, y):
    global start_board_string
    global rows
    global columns
    global board_matrix
    if x < 0 or x >= columns or y < 0 or y >= rows:
        Exception('Invalid coordinate')
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
            field = get_field(x, y + y_offset)
            if field == '':
                bottom_incomplete = False
            elif field == 'l':
                Exception('lamp already placed in column')
            elif field.startswith('b'):
                bottom_incomplete = False
            else:
                set_field(x, y + y_offset, '1')

        if y - y_offset < 0:
            top_incomplete = False
        else:
            field = get_field(x, y - y_offset)
            if field == '':
                top_incomplete = False
            elif field == 'l':
                Exception('lamp already placed in column')
            elif field.startswith('b'):
                top_incomplete = False
            else:
                set_field(x, y - y_offset, '1')

        if x - x_offset < 0:
            left_incomplete = False
        else:
            field = get_field(x - x_offset, y)
            if field == '':
                left_incomplete = False
            elif field == 'l':
                Exception('lamp already placed in column')
            elif field.startswith('b'):
                left_incomplete = False
            else:
                set_field(x - x_offset, y, '1')

        if x + x_offset < 0:
            right_incomplete = False
        else:
            field = get_field(x + x_offset, y)
            if field == '':
                right_incomplete = False
            elif field == 'l':
                Exception('lamp already placed in column')
            elif field.startswith('b'):
                right_incomplete = False
            else:
                set_field(x + x_offset, y, '1')

        x_offset = x_offset + 1
        y_offset = y_offset + 1

def print_board():
    global board_matrix
    for row in board_matrix:
        print('.'.join(row))