def read_input(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()

input_data = read_input('input.txt')
leftList = list()
rightList = list()

# each input has a line with left value and right value seperated by a space, put them in lists
for line in input_data.splitlines():
    if line:
        left, right = line.split('   ')
        leftList.append(int(left))
        rightList.append(int(right))

if len(leftList) != len(rightList):
    raise ValueError('Left list and right list are not the same length')

leftList.sort()
rightList.sort()

distances = list()
for i in range(len(leftList)):
    distances.append(abs(leftList[i] - rightList[i]))

print(sum(distances))