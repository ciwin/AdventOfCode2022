# open the file
with open('input_03.txt') as f:
    # read all lines from the file
    lines = f.readlines()

# Create a dictionary to store the character-integer pairs
asciiASCII = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_int_dict = {}
for i, char in enumerate(asciiASCII):
  char_int_dict[char] = i + 1

substring1 = ""
substring2 = ""

prioSum = 0
for line in lines:
    line = line.strip()
    # print ("line = %s" %line)
    # Calculate the length of the string
    string_length = len(line)
    # print ("string_length = %d" %string_length)
    # Check if the string has an even length
    if string_length % 2 == 0:
        substring1 = line[0:string_length // 2]
        substring2 = line[string_length // 2:]
    else:
        print("Cannot split the string into two substrings of equal length")
        exit
    for char in substring1:
        if char in substring2:
            break
    # print ("Common char is %c with priority %d" % (char, char_int_dict[char]))

    prioSum += char_int_dict[char]

print ("The sum of all priorities is %d" % prioSum)
