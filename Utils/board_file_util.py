def read_board_flat(path) -> str:
    with open(path, encoding='utf-8') as f:
        return ''.join(line.strip() for line in f)
