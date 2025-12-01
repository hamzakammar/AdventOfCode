import re

f = open('Day3/day3.txt', 'r')
code = f.read()

# Updated regex to match only valid mul instructions
# \d{1,3} matches 1-3 digits
pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
matches = re.finditer(pattern, code)

total = 0
validDo = True
print(matches)

for match in matches:
    text = match.group(0)

    if text == "do()":
        validDo = True
    elif text == "don't()":
        validDo = False
    elif text.startswith("mul") and validDo:
        x, y = match.groups()[1], match.groups()[2]
        total += int(x) * int(y)

print("Total:", total)