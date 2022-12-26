with open('input_10_1.txt') as f:
    # read all lines from the file
    lines = f.readlines()

X = 1
cycle = 1
addxCycles = 2
signalStrengthSum = 0

for line in lines:
    line = line.strip()
    input = line.split()
    cmd = input[0]
    if len(input) == 2:
        par = int(input[1])

    if cmd == "noop":
        # print ("noop")
        if cycle in [20, 60, 100, 140, 180, 220]:
            signalStrengthSum += cycle * X
        cycle += 1
    elif cmd == "addx":
        # print ("addx %d" %par)
        addxCycles = 2
        while addxCycles > 0:
            if cycle in [20, 60, 100, 140, 180, 220]:
                signalStrengthSum += cycle * X
            if addxCycles == 1:
                X += par
            cycle += 1
            addxCycles -= 1

print ("cycle             = %d" %(cycle-1))
print ("X                 = %d" %X)
print ("SignalStrengthSum = %d" % signalStrengthSum)
