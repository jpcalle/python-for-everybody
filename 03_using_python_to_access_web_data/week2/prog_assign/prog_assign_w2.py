"""Programming assignment week 2."""

import re

# file = open('D:/Dropbox/Coursera/python_for_everybody/03_using_python_to_access_web_data/week2/prog_assign/regex_sum_42.txt')
file = open('D:/Dropbox/Coursera/python_for_everybody/03_using_python_to_access_web_data/week2/prog_assign/regex_sum_37028.txt')

total = 0

for line in file:
    line_nums = re.findall('[0-9]+', line)
    for str_num in line_nums:
        total += int(str_num)

print("Sum of the number in text: ", total)
