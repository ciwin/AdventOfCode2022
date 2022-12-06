import pprint

# open the file
with open('input_05.txt') as f:
    # read all lines from the file
    lines = f.readlines()
# print (lines)

numOfStacks     = 0
inputStacks     = []
header          = True
startIndexMoves = 0
i               = 0

while i < len(lines):
    line = lines[i]
    inputc = list(line)
    if header == True:
        if header == True and not(inputc[0] == ' ' and inputc[1] == '1'):
            # print (line)
            inputStacks.append(inputc)
        else:
            header = False
            listOfNumbers = line.split()
            numOfStacks = int(listOfNumbers[-1])
            startIndexMoves = i+2
    i += 1

# print ("Num of stacks = %d" % numOfStacks)
# pprint.pprint (inputStacks)

stack = [[] for x in range(numOfStacks)]
for i in range (len(inputStacks)-1, -1, -1):
    # print (inputStacks[i])
    index = 0
    for j in range (numOfStacks):
        if inputStacks[i][index*4+1] != ' ':
            stack[j].append(inputStacks[i][index*4+1])
        index += 1

# pprint.pprint(stack)

i = startIndexMoves
while i < len(lines):
    # print (lines[i])
    token     = lines[i].split()
    numItems  = int(token[1])
    fromStack = int(token[3]) - 1 
    toStack   = int(token[5]) - 1 
    # print ("%d %d %d" % (numItems, fromStack, toStack))
    for k in range (numItems):
        c = stack[fromStack][-1]
        del stack[fromStack][-1]
        stack[toStack].append(c)
    i += 1

# pprint.pprint(stack)

solution = []
for i in range (numOfStacks):
    solution.append(stack[i][-1])

solutionString = ''.join(solution)
print (solutionString)
