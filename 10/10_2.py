with open('input_10_1.txt') as f:
    # read all lines from the file
    lines = f.readlines()

X = 1
sprite = [0,1,2]
cycle = 1
addxCycles = 2
screen = [['.' for x in range(40)] for y in range(6)] 

def draw():
    global cycle
    global sprite
    global screen

    localCycle = (cycle-1) % 240
    y = localCycle // 40
    x = localCycle % 40
    if x == sprite[0] or x == sprite[1] or x == sprite[2]:
        screen[y][x] = '#'
    else:
        screen[y][x] = '.'
    return

for line in lines:
    line = line.strip()
    input = line.split()
    cmd = input[0]
    if len(input) == 2:
        par = int(input[1])

    if cmd == "noop":
        # print ("noop")
        draw()
        cycle += 1
    elif cmd == "addx":
        # print ("addx %d" %par)
        addxCycles = 2
        while addxCycles > 0:
            draw()
            if addxCycles == 1:
                X += par
                sprite[0] = X-1
                sprite[1] = X
                sprite[2] = X+1
            cycle += 1
            addxCycles -= 1

for l in screen:
    print (''.join(l))
