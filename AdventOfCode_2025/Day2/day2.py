#PART 1

with open('input.txt', 'r') as file:
    lines = file.readlines()
    out = 0
    line = lines[0]
    for l in line.split(','):
        first = l.split('-')[0]
        last = l.split('-')[1]
        for i in range(int(first), int(last) + 1):
            i = str(i)
            lenS = len(i)
            if (i[0:lenS//2] == i[lenS//2:lenS]):
                out += int(i)
            
    print(out)

#PART 2

with open('input.txt', 'r') as file:
    lines = file.readlines()
    out = 0
    line = lines[0]
    for l in line.split(','):
        first = l.split('-')[0]
        last = l.split('-')[1]
        for i in range(int(first), int(last) + 1):
            i = str(i)
            lenS = len(i)
            for j in range(1, lenS):
                if ((i[0:j]*(lenS//j)) == i):
                    out += int(i)
                    break
    print(out)