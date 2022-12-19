
forrest      = []
visibleTrees = []

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
        visibleList.append(-1)
    forrest.append(intList)
    visibleTrees.append(visibleList)

# print (forrest)

numLines = len(forrest)
numCol   = len(forrest[0])

for line in range(numLines):
    for col in range(numCol):
        vTrees = 0
        c = col
        # look left:
        c = col
        sight = True
        while c > 0:
            if sight:
                vTrees += 1
                if forrest[line][col] <= forrest[line][c-1]:
                    sight = False 
            c -= 1
        score = vTrees
        # look right:
        vTrees = 0
        c = col
        sight = True
        while c < (numCol-1):
            if sight:
                vTrees += 1
                if forrest[line][col] <= forrest[line][c+1]:
                    sight = False 
            c += 1
        score *= vTrees
        # look up:
        vTrees = 0
        l = line
        sight = True
        while l > 0:
            if sight:
                vTrees += 1
                if forrest[line][col] <= forrest[l-1][col]:
                    sight = False 
            l -= 1
        score *= vTrees
        # look down:
        vTrees = 0
        l = line
        sight = True
        while l < (numLines-1):
            if sight:
                vTrees += 1
                if forrest[line][col] <= forrest[l+1][col]:
                    sight = False 
            l += 1
        score *= vTrees
        visibleTrees[line][col] = score

highestTree = -1
for l in visibleTrees:
    for t in l:
        if t > highestTree:
            highestTree = t

print ("Highest scenic sccore is %d" %highestTree)
