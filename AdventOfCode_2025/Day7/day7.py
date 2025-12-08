with open("input.txt") as file:
    diagram = [line.rstrip('\n') for line in file.readlines()]
width, height = len(diagram[0]), len(diagram)

#Part 1 
beam_idxs = {diagram[0].find('S')}
split_count = 0
for i in range(1, height):
    current_beam_idxs = list(beam_idxs)
    line = diagram[i]
    for b in current_beam_idxs:
        if line[b] == "^":
            split_count += 1
            beam_idxs.remove(b)
            left = b - 1
            right = b + 1
            if left >= 0:
                beam_idxs.add(left)
            if right < width:
                beam_idxs.add(right)
print(split_count)

#Part 2
beam_idxs = {diagram[0].find('S')}
timeline_count = 0

def count_timelines(node: tuple[int, int]):
    row, col = node[0], node[1]
    if row + 1 == len(diagram):
        return 1
    if diagram[row][col] == "^":
        left, right =  (row, col - 1), (row, col + 1)
        left_count, right_count = 0, 0
        if left[1] >= 0:
            left_count = count_timelines(left)
        if right[1] < width:
            right_count = count_timelines(right)
        return left_count + right_count
    else:
        return count_timelines((row+1, col))
    
print(count_timelines((0, diagram[0].find('S'))))