# open the file
with open('input_04.txt') as f:
    # read all lines from the file
    lines = f.readlines()

countOverlapping = 0
# 34-82,33-81
for line in lines:
    elfs = line.split(",")
    elf1Section = elfs[0].split("-")
    elf2Section = elfs[1].split("-")
    elf1SectionStart = int(elf1Section[0].strip())
    elf1SectionEnd   = int(elf1Section[1].strip())
    elf2SectionStart = int(elf2Section[0].strip())
    elf2SectionEnd   = int(elf2Section[1].strip())
    
    # overlap = 0
    if ((elf2SectionStart >= elf1SectionStart) and (elf2SectionEnd <= elf1SectionEnd)):
        # elf2Section is included in elf1Section
        # overlap = elf2SectionEnd - elf2SectionStart + 1
        countOverlapping += 1
    elif ((elf1SectionStart >= elf2SectionStart) and (elf1SectionEnd <= elf2SectionEnd)):
        # elf1Section is included in elf2Section
        # overlap = elf1SectionEnd - elf1SectionStart + 1
        countOverlapping += 1
    elif ((elf2SectionStart <= elf1SectionEnd) and (elf2SectionEnd > elf1SectionEnd)):
        # elf2Section is overlapping elf1Section on the right
        # overlap = elf2SectionStart - elf1SectionEnd + 1
        countOverlapping += 1
    elif ((elf1SectionStart <= elf2SectionEnd) and (elf1SectionEnd > elf2SectionEnd)):
        # elf1Section is overlapping elf2Section on the right
        # overlap = elf1SectionStart - elf2SectionEnd + 1
        countOverlapping += 1
    
# print ("%d-%d,%d-%d" %(elf1SectionStart, elf1SectionEnd, elf2SectionStart, elf2SectionEnd))
print ("Amount of overlapping: %d" %countOverlapping)
