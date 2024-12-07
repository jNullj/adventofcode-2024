from shared.fileUtil import read_input
import re

input_data = read_input('q3/input.txt')

# remove all mul inside "don't()"
pattern = r'don\'t\(\).*?do\(\)'
input_data = re.sub(pattern, '', input_data, flags=re.DOTALL)
# remove last don't if exists
pattern = r'don\'t\(\).*$'
input_data = re.sub(pattern, '', input_data, flags=re.DOTALL)

# find solution like in part1 with the cleaned input
pattern = r'mul\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)'
matches = re.findall(pattern, input_data)
multiplications = [(int(a)* int(b)) for a, b in matches]
print(sum(multiplications))
