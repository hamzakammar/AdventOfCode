#Part 1
with open('input.txt', 'r') as file:
    lines = file.readlines()
    out = 0
    for line in lines:
        firstMax = 0
        for i in range(len(line)-2):
            if line[i] > line[firstMax]:
                firstMax = i
        secondMax = firstMax+1
        for j in range(firstMax+1, len(line)-1):
            if line[j] > line[secondMax]:
                secondMax = j
        out += (int(line[firstMax])*10 + int(line[secondMax]))
    print(out)

#Part 2
with open('input.txt', 'r') as file:
    lines = file.readlines()
    out = 0
    for line in lines:
        line = line.strip()
        total = 0
        start = 0
        for i in range(12):
            remaining_needed = 12 - i - 1
            end = len(line) - remaining_needed
            max_digit = -1
            max_pos = start
            for j in range(start, end):
                if int(line[j]) > max_digit:
                    max_digit = int(line[j])
                    max_pos = j
            
            total = total * 10 + max_digit
            start = max_pos + 1
        
        out += total
    print(out)