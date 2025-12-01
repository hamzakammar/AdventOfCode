f = open('Day6/Day6.txt', 'r')
code = f.read()

# Convert each line from a string to a list of characters
lines = [list(line) for line in code.split("\n")]

#Find where the '^' is
direction = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '^':
            posI = i
            posJ = j
            #Up 0, Right 1, Down 2, Left 3
#Make an X where it has already been
inBounds = True
distinctPos = 1


while inBounds:
    match direction:
        case 0:
            try:
                if lines[posI-1][posJ] != "#":
                    print(lines[posI][posJ])
                    lines[posI][posJ] = "X"
                    posI -= 1

                    if lines[posI][posJ] != "X":
                        distinctPos += 1
                else:
                    direction += 1
            except:
                inBounds = False


        case 1:
            try:
                if lines[posI][posJ+1] != "#":
                    lines[posI][posJ] = "X"
                    posJ += 1
                    if lines[posI][posJ] != "X":
                        distinctPos += 1
                else:
                    direction += 1
            except:
                inBounds = False
        case 2:
            try:
                if lines[posI+1][posJ] != "#":
                    lines[posI][posJ] = "X"
                    posI += 1
                    if lines[posI][posJ] != "X":
                        distinctPos += 1
                else:
                    direction += 1
            except:
                inBounds = False
        case 3:
            try:
                if lines[posI][posJ-1] != "#":
                    lines[posI][posJ] = "X"
                    posJ -= 1
                    if lines[posI][posJ] != "X":
                        distinctPos += 1
                else:
                    direction = 0      
            except:
                inBounds = False
print(distinctPos)
        
