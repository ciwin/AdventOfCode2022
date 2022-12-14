# open the file
# from ctypes import sizeof

# Global Variables:
visitedPlaces = []
head          = [0,0]
tail          = [0,0]

def savePlace(pos):
    global visitedPlaces
    x = pos[0]
    y = pos[1]
    if not pos in visitedPlaces:
        visitedPlaces.append([x,y])
    return

def moveHead(dir):
    global head
    if   dir == "L":
        head[0] -= 1
    elif dir == "R":
        head[0] += 1
    elif dir == "U":
        head[1] += 1
    elif dir == "D":
        head[1] -= 1
    else:
        print("ERROR: Wrong dir read!")
    return

def moveTail():
    global head
    global tail
    if head[0] == tail[0] and head[1] == tail[1]:
        return
    if ((head[0] == tail[0] and head[1] == tail[1]+1) or  #  T and H are adjacent
        (head[0] == tail[0] and head[1] == tail[1]-1) or
        (head[1] == tail[1] and head[0] == tail[0]+1) or
        (head[1] == tail[1] and head[0] == tail[0]-1) or
        (head[0] == tail[0]+1 and head[1] == tail[1]+1) or  # T and H are diagonally adjacent
        (head[0] == tail[0]-1 and head[1] == tail[1]-1) or
        (head[0] == tail[0]+1 and head[1] == tail[1]-1) or
        (head[0] == tail[0]-1 and head[1] == tail[1]+1)):
        return
    if (head[0] == tail[0] and head[1] == tail[1]+2):
        tail[1] += 1
        return
    if (head[0] == tail[0] and head[1] == tail[1]-2):
        tail[1] -= 1
        return
    if (head[1] == tail[1] and head[0] == tail[0]+2):
        tail[0] += 1
        return
    if (head[1] == tail[1] and head[0] == tail[0]-2):
        tail[0] -= 1
        return
    if head[0] < tail[0]:
        tail[0] -= 1
    else:
        tail[0] += 1
    if head[1] < tail[1]:
        tail[1] -= 1
    else:
        tail[1] += 1
    return

with open('input_09.txt') as f:
    # read all lines from the file
    lines = f.readlines()

savePlace(tail)

for line in lines:
    line = line.strip()
    input = line.split()
    dir = input[0]
    steps = int(input[1])
    # print ("Dir: %s Steps: %d" %(dir, steps))
    for i in range(steps):
        moveHead(dir)
        moveTail()
        # print ("Head: %d %d - Tail: %d %d" %(head[0], head[1], tail[0], tail[1]))
        savePlace(tail)

# print ("Head is at %d %d" %(head[0], head[1]))
# print (visitedPlaces)
print ("Tail has visited %d different places" %len(visitedPlaces))
