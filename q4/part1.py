from shared.fileUtil import read_input
from q4.mapManipulation import get_map_window, WindowOutOfBoundsException, diag_str_map

input_data = read_input('q4/input.txt')

# remove trailing newline
input_data = input_data.strip()

y = 0
x = 0
word_map = {}
for char in input_data:
    if char == '\n':
        y += 1
        x = 0
        continue
    word_map[(x, y)] = char
    x += 1

search_word = 'XMAS'
window_size = len(search_word)
result = 0
max_x = max(k[0] for k in word_map.keys())
max_y = max(k[1] for k in word_map.keys())

for y in range(0, max_y+1):
    for x in range(0, max_x+1):
        try:
            horiz_win = get_map_window(word_map, x, y, window_size, 1)
            if ''.join(horiz_win.values()) == search_word:
                result += 1
            if ''.join(horiz_win.values()) == search_word[::-1]:
                result += 1
        except WindowOutOfBoundsException:
            pass
        try:
            vert_win = get_map_window(word_map, x, y, 1, window_size)
            if ''.join(vert_win.values()) == search_word:
                result += 1
            if ''.join(vert_win.values()) == search_word[::-1]:
                result += 1
        except WindowOutOfBoundsException:
            pass
        try:
            diag_win = get_map_window(word_map, x, y, window_size, window_size)
            diag_str = diag_str_map(diag_win)
            diag_str_cross = diag_str_map(diag_win, cross=True)
            if diag_str == search_word:
                result += 1
            if diag_str == search_word[::-1]:
                result += 1
            if diag_str_cross == search_word:
                result += 1
            if diag_str_cross == search_word[::-1]:
                result += 1
        except WindowOutOfBoundsException:
            pass

print(result)
