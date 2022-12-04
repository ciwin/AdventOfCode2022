# open the file
with open('input_01.txt') as f:
    # read all lines from the file
    lines = f.readlines()

# initialize an empty list to store the integers
elfList = []

# iterate over the lines
numElf  = -1
numFood = 0
for line in lines:
    # strip the newline character from the line
    line = line.strip()
    if line == '':
        numElf += 1
        foodList = []
        elfList.append(foodList)
        # print ("Elf No. %d:" % numElf)
    else:
        # convert the line to an integer and append it to the list
        elfList[numElf].append(int(line))
# print the list of integers
numElf = -1
caloriesPerElf = []
sumCalories    = 0
for e in elfList:
    numElf += 1
    # print ("Elf No. %d:" % numElf)
    sumCalories = 0
    for f in e:
        sumCalories += f
        # print (f)
    caloriesPerElf.append(sumCalories) 
# print(int_list)
# print (caloriesPerElf)

# Find the Elf with the maximun calories:
highestCalories = max(caloriesPerElf)
print ("The Elf with the highest Calories is carrying %d calories" % highestCalories)

######################################################################################
#### Second Star
######################################################################################

sortedCaloriesPerElf = sorted(caloriesPerElf, reverse=True)

print (sortedCaloriesPerElf)

top3ElfCalories = sortedCaloriesPerElf[0] + sortedCaloriesPerElf[1] + sortedCaloriesPerElf[2]
print ("Calories of the top 3 Elfs: %d" %top3ElfCalories)
