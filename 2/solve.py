from shared.fileUtil import read_input

def is_report_increase_decrease(report: list[int]) -> tuple[bool, int]:
    # does all values only increase/decrease
    if report[0] < report[1]:
        direction = 'increase'
    elif report[0] > report[1]:
        direction = 'decrease'
    else:
        return False, 1 # note, if at edge can be both
    for i in range(2, len(report)):
        if direction == 'increase' and report[i] < report[i-1]:
            return False, i
        elif direction == 'decrease' and report[i] > report[i-1]:
            return False, i
    return True, -1

def is_report_valid_step_size(report: list[int], min: int, max: int) -> tuple[bool, int]:
    # is the step size within the min and max
    for i in range(1, len(report)):
        step_size = abs(report[i] - report[i-1])
        if step_size < min or step_size > max:
            return False, i
    return True, -1

def is_report_safe(report: list[int]) -> bool:
    # check if the report is safe
    # IDEA we can combine the functions for efficiency
    # as step size incode the direction
    valid, i = is_report_increase_decrease(report)
    if not valid:
        return False, i
    valid, i = is_report_valid_step_size(report, 1, 3)
    if not valid:
        return False, i
    return True, -1

def extract_reports(input_data: str) -> list[list[int]]:
    # extract from text input
    reports = []
    for line in input_data.split('\n'):
        if line == '':
            continue
        report = line.split(' ')
        report = [int(val) for val in report]
        reports.append(report)
    return reports

input_data = read_input('2/input.txt')
reports = extract_reports(input_data)

# how many reports are safe
safe_reports = 0
for report in reports:
    safe, i = is_report_safe(report)
    if safe:
        safe_reports += 1
print(safe_reports)