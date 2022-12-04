# open the file
with open('input_02.txt') as f:
    # read all lines from the file
    lines = f.readlines()

score = 0
for line in lines:
    signs = line.split()
    # print (signs)
    if   (signs[0] == 'A' and signs[1] == 'X'):
        score += 4
    elif (signs[0] == 'B' and signs[1] == 'X'):
        score += 1
    elif (signs[0] == 'C' and signs[1] == 'X'):
        score += 7
    elif (signs[0] == 'A' and signs[1] == 'Y'):
        score += 8
    elif (signs[0] == 'B' and signs[1] == 'Y'):
        score += 5
    elif (signs[0] == 'C' and signs[1] == 'Y'):
        score += 2
    elif (signs[0] == 'A' and signs[1] == 'Z'):
        score += 3
    elif (signs[0] == 'B' and signs[1] == 'Z'):
        score += 9
    elif (signs[0] == 'C' and signs[1] == 'Z'):
        score += 6
    else:
        print ("ERROR in reading the line!")

# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# Opp.          You          Score1 Win Score2 Total Score    
# A = Rock      X = Rock     1      =   3       4
# B = Paper     X = Rock     1      O   0       1
# C = Scissors  X = Rock     1      Y   6       7
# A = Rock      Y = Paper    2      Y   6       8
# B = Paper     Y = Paper    2      =   3       5
# C = Scissors  Y = Paper    2      O   0       2
# A = Rock      Z = Scissors 3      O   0       3
# B = Paper     Z = Scissors 3      Y   6       9
# C = Scissors  Z = Scissors 3      =   3       6

print ("The total score is %d" % score)
