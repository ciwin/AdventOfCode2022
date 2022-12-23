# open the file
# from ctypes import sizeof

visitedPlaces = []

def savePlace (pos):
    global visitedPlaces
    if not pos in visitedPlaces:
        visitedPlaces.append(pos)
    return

with open('input_09_test.txt') as f:
    # read all lines from the file
    lines = f.readlines()

x = 0
y = 0
pos = [0,0]
savePlace(pos)

for line in lines:
    line = line.strip()
    input = line.split()
    dir = input[0]
    steps = int(input[1])
    print ("Dir: %s Steps: %d" %(dir, steps))
