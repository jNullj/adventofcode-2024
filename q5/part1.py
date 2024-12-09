from shared.fileUtil import read_input
from q5.base import RuleSet, ManualUpdate

input = read_input('q5/input.txt')
input = input.strip().split('\n\n')
input_rules = input[0].split('\n')
input_updates = input[1].split('\n')

rules = RuleSet(input_rules)
updates = [ManualUpdate(update) for update in input_updates]

result = 0
for update in updates:
    if rules.testUpdate(update):
        result += update.middlePageNum()

print(result)