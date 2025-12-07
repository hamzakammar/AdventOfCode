import re 
import math

with open("input.txt") as file:
    lines = [line.rstrip('\n') for line in file.readlines()]
    n = len(lines[0])

    total = 0
    i = 0
    while i < n:
        if all(lines[row][i] == ' ' for row in range(len(lines))):
            i += 1
            continue
        problem_end = i
        while problem_end < n and not all(lines[row][problem_end] == ' ' for row in range(len(lines))):
            problem_end += 1
         
        operator = lines[-1][i:problem_end].strip()
        numbers = []
        for row in range(len(lines) - 1):
            num_str = lines[row][i:problem_end].strip()
            if num_str:
                numbers.append(int(num_str))
        if operator == '+':
            result = 0
            for num in numbers:
                result += num
        elif operator == '*':
            result = 1
            for num in numbers:
                result *= num
        total += result
        i = problem_end
    print(total)

#Part 2:
with open("input.txt") as file:
    data_list = file.read().splitlines()
    col_len_list = [len(col) for col in re.split(r"\s(?=[+\*])", data_list[-1])]
    col_list = []
    for row in data_list:
        cols = []
        idx = 0
        for col_len in col_len_list:
            idx_next = idx + col_len
            cols.append(row[idx:idx_next])
            idx = idx_next + 1
        col_list.append(cols)
    col_list = list(zip(*col_list))
    parsed_data = col_list
    total_value = 0

    for idx, col in enumerate(parsed_data):
        rev_col = list(zip(*[list(num[::-1]) for num in col[:-1]]))
        join_numbers = [int("".join(num).strip()) for num in rev_col]
        answer = 0
        match col[-1].strip():
            case "+":
                answer = sum(join_numbers)
            case "*":
                answer = math.prod(join_numbers)
        print("Expression {} equals {}.".format(idx, answer))
        total_value += answer
    print(total_value)
