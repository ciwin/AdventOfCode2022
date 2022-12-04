# open the file
with open('input_04.txt') as f:
    # read all lines from the file
    lines = f.readlines()

countAssigns = 0
# 34-82,33-81
for line in lines:
    elfs = line.split(",")
    elf1Section = elfs[0].split("-")
    elf2Section = elfs[1].split("-")
    elf1SectionStart = int(elf1Section[0].strip())
    elf1SectionEnd   = int(elf1Section[1].strip())
    elf2SectionStart = int(elf2Section[0].strip())
    elf2SectionEnd   = int(elf2Section[1].strip())
    
    if (((elf1SectionStart <= elf2SectionStart) and (elf1SectionEnd >= elf2SectionEnd)) or
        ((elf2SectionStart <= elf1SectionStart) and (elf2SectionEnd >= elf1SectionEnd))):
        countAssigns += 1
        # print ("%d-%d,%d-%d" %(elf1SectionStart, elf1SectionEnd, elf2SectionStart, elf2SectionEnd))

print ("Assignment Pairs fully contained: %d" %countAssigns)
