
forrest      = []
visibleTrees = []

def cTrees(dir):
    numLines = len(forrest)
    numCol   = len(forrest[0])
    if dir == "south":    
        for c in range (numCol):
            actHigh = -1
            for l in range (numLines):
                if forrest[c][l] > actHigh:
                    visibleTrees[c][l] = True
                    actHigh = forrest[c][l]
        return
    if dir == "north":
        for c in range (numCol):
            actHigh = -1
            for l in reversed(range (numLines)):
                if forrest[c][l] > actHigh:
                    visibleTrees[c][l] = True
                    actHigh = forrest[c][l]
        return
    if dir == "east":    
        for l in range (numLines):
            actHigh = -1
            for c in range (numCol):
                if forrest[c][l] > actHigh:
                    visibleTrees[c][l] = True
                    actHigh = forrest[c][l]
        return
    if dir == "west":
        for l in range (numLines):
            actHigh = -1
            for c in reversed(range(numCol)):
                if forrest[c][l] > actHigh:
                    visibleTrees[c][l] = True
                    actHigh = forrest[c][l]
        return

# open the file
from ctypes import sizeof
with open('input_08.txt') as f:
    # read all lines from the file
    lines = f.readlines()

for line in lines:
    line = line.strip()
    charList = list(line)
    intList     = []
    visibleList = []
    for c in charList:
        i = int(c)
        intList.append(i)
        visibleList.append(False)
    forrest.append(intList)
    visibleTrees.append(visibleList)

# print (forrest)

cTrees ("north")
cTrees ("east")
cTrees ("south")
cTrees ("west")

# print (visibleTrees)

numVisibleTrees = 0
for l in visibleTrees:
    for t in l:
        if t:
            numVisibleTrees += 1

print ("Number of visible trees: %d" %numVisibleTrees)
