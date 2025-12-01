def read_grid(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f]

def check_sequence(grid, row, col, dr, dc, target="XMAS"):
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
        return False
        
    for i in range(len(target)):
        r, c = row + i*dr, col + i*dc
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            return False
            
    word = ''
    for i in range(len(target)):
        r, c = row + i*dr, col + i*dc
        word += grid[r][c]
    
    return word == target

def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [
        (0,1),  
        (1,1),  
        (1,0),  
        (1,-1),  
        (0,-1),  
        (-1,-1), 
        (-1,0),  
        (-1,1)
    ]
    
    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if check_sequence(grid, row, col, dr, dc):
                    count += 1
                    
    return count

grid = read_grid("Day4/day4.txt")
total = count_xmas(grid)
print(total)
