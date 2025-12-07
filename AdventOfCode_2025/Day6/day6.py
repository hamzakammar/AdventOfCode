with open("input.txt") as file:
    lines = [line.rstrip('\n') for line in file.readlines()]
    n = len(lines[0])

    sum = 0
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
        sum += result
        i = problem_end
    print(sum)