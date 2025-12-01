f = open('day1.txt', 'r')
code = f.read()

fulllist = code.split()

left = fulllist[::2]
right = fulllist[1::2]

left.sort()
right.sort()

totalDist = 0
for i in range(len(left)):
    totalDist += abs(int(right[i])-int(left[i]))

print("First: ", totalDist)

#####################


left2 = fulllist[::2]
right2 = fulllist[1::2]

similarityScore = 0

for i in range(len(left2)):
    for j in range(len(right2)):
        if left2[i] == right2[j]:
            similarityScore += int(left2[i])

print(similarityScore)
