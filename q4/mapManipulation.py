class WindowOutOfBoundsException(Exception):
    pass

def get_map_window(m: dict[(int, int), str], x: int, y: int, window_size_x: int, window_size_y: int) -> dict[(int, int), str]:
    window = {}
    max_x = max(k[0] for k in m.keys())
    max_y = max(k[1] for k in m.keys())
    if x < 0 or y < 0:
        raise WindowOutOfBoundsException()
    if x + window_size_x > max_x + 1 or y + window_size_y > max_y + 1:
        raise WindowOutOfBoundsException()
    for i in range(x, x + window_size_x):
        for j in range(y, y + window_size_y):
            window[(i-x, j-y)] = m[(i, j)]
    return window

def diag_str_map(m: dict[(int, int), str], cross=False) -> str:
    x = 0
    max_x = max(k[0] for k in m.keys())
    max_y = max(k[1] for k in m.keys())
    if cross:
        y = max_y
    else:
        y = 0
    diag = ''
    while x <= max_x and y <= max_y:
        diag += m.get((x, y), '')
        if cross:
            x += 1
            y -= 1
        else:
            x += 1
            y += 1
    return diag