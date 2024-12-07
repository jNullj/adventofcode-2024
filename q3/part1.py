from shared.fileUtil import read_input
import re

input_data = read_input('q3/input.txt')

pattern = r'mul\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)'
matches = re.findall(pattern, input_data)
multiplications = [(int(a)* int(b)) for a, b in matches]
print(sum(multiplications))