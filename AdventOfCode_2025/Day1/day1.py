#PART 1
with open('input.txt', 'r') as file:
    lines = file.readlines()
    count = 0
    start = 50
    for line in lines:
        num = int(line.strip()[1:])
        dir = line.strip()[0]
        if dir == 'R':
            start += num
        elif dir == 'L':
            start -= num
        start %= 100
        if start == 0:
            count += 1
    print(count)
        
#PART 2

with open('input.txt', 'r') as file:
    lines = file.readlines()
    count = 0

    rotations = []
    dial = 50
    for line in lines:
        direction = line[0]
        clicks = line[1:]
        if direction == 'L':
            rotations.append(int(clicks) * -1)
        else:
            rotations.append(int(clicks))
    for clicks in rotations:
        new_position = dial + clicks
        if new_position > 0:
            count += new_position // 100
        elif new_position == 0:
            count += 1
        else:
            count += ((100 - dial) % 100 + abs(clicks)) // 100
        dial = (dial + clicks) % 100
    print(count)