from shared.fileUtil import read_input

def is_report_increase_decrease(report: list[int]) -> bool:
    # does all values only increase/decrease
    if report[0] < report[1]:
        direction = 'increase'
    elif report[0] > report[1]:
        direction = 'decrease'
    else:
        return False
    for i in range(2, len(report)):
        if direction == 'increase' and report[i] < report[i-1]:
            return False
        elif direction == 'decrease' and report[i] > report[i-1]:
            return False
    return True

def is_report_valid_step_size(report: list[int], min: int, max: int) -> bool:
    # is the step size within the min and max
    for i in range(1, len(report)):
        step_size = abs(report[i] - report[i-1])
        if step_size < min or step_size > max:
            return False
    return True

def is_report_safe(report: list[int]) -> bool:
    # check if the report is safe
    # IDEA we can combine the functions for efficiency
    # as step size incode the direction
    if not is_report_increase_decrease(report):
        return False
    if not is_report_valid_step_size(report, 1, 3):
        return False
    return True

input_data = read_input('2/input.txt')

# extract from text input
reports = []
for line in input_data.split('\n'):
    if line == '':
        continue
    report = line.split(' ')
    print(report)
    report = [int(val) for val in report]
    reports.append(report)

# how many reports are safe
safe_reports = 0
for report in reports:
    if is_report_safe(report):
        safe_reports += 1
print(safe_reports)