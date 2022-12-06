# open the file
with open('input_06.txt') as f:
    # read all lines from the file
    lines = f.readlines()
# print (lines[0])
signal = list(lines[0])
# print (signal)

found = False
for c in range (len(signal)):
    if c < 12:
        continue
    if len(set(signal[c-13:c+1])) == 14:
        found = True
        break

if found:
    c += 1
    print ("Marker appears after the %d th position" % c)
    # print ("Marker = %s" % signal[c-3:c+1])
