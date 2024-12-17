f = open('Day5/day5.txt', 'r')
code = f.read()

listOfRules = code.split("\n")[0:1176]
listOfUpdates = code.split("\n")[1178:]

dictOfRules = dict()
for i in range(len(listOfRules)):
    if int(listOfRules[i][0:2]) not in dictOfRules:
        dictOfRules[int(listOfRules[i][0:2])] = []  # Initialize list if key not present
    dictOfRules[int(listOfRules[i][0:2])].append(int(listOfRules[i][3:5]))

