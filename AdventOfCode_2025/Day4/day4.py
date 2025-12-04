def checkNeighbours(grid, x, y):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1), (1, 1), (1, -1)]  # Up, Down, Left, Right, Top Right, Top Left, Bottom Right, Bottom Left 
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == '@':
                count += 1
    if count >= 4:
        return False
    return True


#PART 1
with open('input.txt', 'r') as file:
    lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '@':
                if checkNeighbours(grid, i, j):
                    count += 1
    print(count)

#PART 2
with open('input.txt', 'r') as file:
    lines = file.readlines()
    grid = [list(line.strip()) for line in lines]
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    newGrid = [row.copy() for row in grid]
    changed = True
    while changed:
        changed = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '@':
                    if checkNeighbours(grid, i, j):
                        newGrid[i][j] = '.'
                        changed = True
                        count += 1
        grid = [row.copy() for row in newGrid]
        if not changed:
            break
    print(count)

