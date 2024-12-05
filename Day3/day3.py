import re

f = open('Day3/day3.txt', 'r')
code = f.read()

# Updated regex to match only valid mul instructions
# \d{1,3} matches 1-3 digits
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, code)

total = 0
for x, y in matches:
    total += int(x) * int(y)

print("Total:", total)