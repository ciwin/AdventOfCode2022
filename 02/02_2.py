# open the file
with open('input_02.txt') as f:
    # read all lines from the file
    lines = f.readlines()

score = 0
for line in lines:
    signs = line.split()
    # print (signs)

# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win.
# Opp.          Sign            You     
# A = Rock      X = you lose    Scissors = C    
# B = Paper     X = you lose    Rock     = A   
# C = Scissors  X = you lose    Paper    = B
# A = Rock      Y = draw        Rock     = A
# B = Paper     Y = draw        Paper    = B
# C = Scissors  Y = draw        Scissors = C
# A = Rock      Z = you win     Paper    = B
# B = Paper     Z = you win     Scissors = C
# C = Scissors  Z = you win     Rock     = A
    if   (signs[0] == 'A' and signs[1] == 'X'):
        signs[1] = 'C'
    elif (signs[0] == 'B' and signs[1] == 'X'):
        signs[1] = 'A'
    elif (signs[0] == 'C' and signs[1] == 'X'):
        signs[1] = 'B'
    elif (signs[0] == 'A' and signs[1] == 'Y'):
        signs[1] = 'A'
    elif (signs[0] == 'B' and signs[1] == 'Y'):
        signs[1] = 'B'
    elif (signs[0] == 'C' and signs[1] == 'Y'):
        signs[1] = 'C'
    elif (signs[0] == 'A' and signs[1] == 'Z'):
        signs[1] = 'B'
    elif (signs[0] == 'B' and signs[1] == 'Z'):
        signs[1] = 'C'
    elif (signs[0] == 'C' and signs[1] == 'Z'):
        signs[1] = 'A'
    else:
        print ("ERROR in reading the line!")

## Rock defeats Scissors, Scissors defeats Paper, Paper defeats Rock.
# Opp.          You          Score1 Win Score2 Total Score    
# A = Rock      A = Rock     1      =   3       4
# B = Paper     A = Rock     1      O   0       1
# C = Scissors  A = Rock     1      Y   6       7
# A = Rock      B = Paper    2      Y   6       8
# B = Paper     B = Paper    2      =   3       5
# C = Scissors  B = Paper    2      O   0       2
# A = Rock      C = Scissors 3      O   0       3
# B = Paper     C = Scissors 3      Y   6       9
# C = Scissors  C = Scissors 3      =   3       6

    if   (signs[0] == 'A' and signs[1] == 'A'):
        score += 4
    elif (signs[0] == 'B' and signs[1] == 'A'):
        score += 1
    elif (signs[0] == 'C' and signs[1] == 'A'):
        score += 7
    elif (signs[0] == 'A' and signs[1] == 'B'):
        score += 8
    elif (signs[0] == 'B' and signs[1] == 'B'):
        score += 5
    elif (signs[0] == 'C' and signs[1] == 'B'):
        score += 2
    elif (signs[0] == 'A' and signs[1] == 'C'):
        score += 3
    elif (signs[0] == 'B' and signs[1] == 'C'):
        score += 9
    elif (signs[0] == 'C' and signs[1] == 'C'):
        score += 6
    else:
        print ("ERROR in reading the line!")

print ("The total score is %d" % score)
