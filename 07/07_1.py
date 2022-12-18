# open the file
from ctypes import sizeof
with open('input_07.txt') as f:
    # read all lines from the file
    lines = f.readlines()

# print (lines[0])

rootDir = None
dirList = []

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def getSize(self):
        return self.size

class Dir:
    def __init__(self, name, parentDir):
        self.name      = name
        self.parentDir = parentDir
        self.dirList  = []
        self.fileList = []

    def addDir(self, name):
        for d in self.dirList:
            if name == d.name:
                return False
        newDir = Dir(name, self)
        self.dirList.append(newDir)
        return True
    
    def addFile(self, name, size):
        for f in self.fileList:
            if name == f.name:
                return False
        newFile = File(name, size)
        self.fileList.append(newFile)
        return True

    def gotoDir(self, name):
        if name == '/':
            return rootDir
        if name == "..":
            return self.parentDir
        for d in self.dirList:
            if name == d.name:
                return d
        return None

    def calcDirSize(self):
        global dirList
        size = 0
        for f in self.fileList:
            size += f.size
        for d in self.dirList:
            size += d.calcDirSize()
        dir = {
            'name' : self.name,
            'size' : size
        }
        dirList.append(dir)
        #print ("dir %s with size %d" %(self.name, size))
        # totalSizeSmaller += size
        return size
        
rootDir = Dir("/", None)
actDir  = rootDir

# myFile = File("test.txt", 100)
# print ("Filesize: %d" %myFile.getSize())

index = -1
while index+1 < len(lines):
    index += 1
    line = lines[index]
    command = line.split()
    # print (command)
    if command[0] == "$" and command[1] == "cd":
        newDir = actDir.gotoDir(command[2])
        if newDir == None:
            print ("ERROR: Directory %s not found!" %command[2])
            continue
        actDir = newDir
        # print ("  -- cd to dir %s" %actDir.name)
        continue
    if command[0] == "dir":
        if not actDir.addDir(command[1]):
            print ("ERROR: Directory already exists!")
        # print ("  -- Added new dir = %s" %command[1])
        continue
    if command[0] != "dir" and command[0] != "$":
        if not actDir.addFile(command[1], int(command[0])):
            print ("ERROR: File already exists!")
        # print ("  -- Added new file = %s" %command[1])

rootSize    = rootDir.calcDirSize()
freeSpace   = 70000000 - rootSize
neededSpace = 30000000 - freeSpace

print ("Needed Space: %d" %neededSpace)
for d in dirList:
    print(d)

bestDir = None
delete  = rootSize
for d in dirList:
    if d["size"] >= neededSpace and d["size"] <= delete:
        delete  = d["size"]
        bestDir = d

print ("Dir to delete: %s (size: %d)" %(bestDir["name"], bestDir["size"]))
# print ("Total free space after delete: %d" %(freeSpace + bestDir["size"]))

# My solution is nbnzfc, but this seems to be wrong!
