from shared.fileUtil import read_input
from q2.solve import is_report_safe, extract_reports

input_data = read_input('q2/input.txt')
reports = extract_reports(input_data)

# how many reports are safe
safe_reports = 0
for report in reports:
    safe, i = is_report_safe(report)
    i = 0
    # The Problem Dampener
    while not safe and i < len(report):
        dampedReport = report.copy()
        dampedReport.pop(i)
        safe, id = is_report_safe(dampedReport)
        i += 1
    if safe:
        safe_reports += 1
print(safe_reports)
