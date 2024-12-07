def read_input(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()

input_data = read_input('input.txt')
leftList = list()
rightList = list()

def frequency(l: list):
    result = dict()
    for i in l:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

def similarityScore(left: list, freq: dict):
    result = 0
    for i in left:
        if i in freq:
            result += i * freq[i]
    return result

# each input has a line with left value and right value seperated by a space, put them in lists
for line in input_data.splitlines():
    if line:
        left, right = line.split('   ')
        leftList.append(int(left))
        rightList.append(int(right))

if len(leftList) != len(rightList):
    raise ValueError('Left list and right list are not the same length')

rightFreq = frequency(rightList)
print(similarityScore(leftList, rightFreq))