import re
class node:
    def __init__(self, parent=None , name = "/"):
        self.name = name
        self.size = 0
        self.childs = list()
        self.parent = parent
    
    def add(self, node):
        self.childs.append(node)

    def increase(self, num):
        self.size += num

### GLOBALS ###
total = 0
###############

def SumTree(root):
    if(len(root.childs) != 0):
        for child in root.childs:
            SumTree(child)
        for child in root.childs:
                root.increase(child.size)

def findTotal(root):
    global total
    if(len(root.childs) == 0):
        if(root.size <= 100000):
            total += root.size
    else:
        for child in root.childs:
            if(root.size <= 100000):
                total += root.size
            findTotal(child)

def main():
    global total
    f = open("input", "r")
    f.readline()
    head = node()
    root = head
    for lines in f:
        if lines[0:4] == "$ cd":
            if(lines[5] == "."):
                head = head.parent
            else:
                for child in head.childs:
                    if child.name == lines[5:].strip():
                        head = child
                        break
        elif lines[0:3] == "dir":
            head.add(node(head, lines[4:].strip()))
            pass
        elif lines[0:4] != "$ ls":
            x = re.findall(r'\d+', lines)
            head.increase(int(x[0]))
    
    SumTree(root)
    findTotal(root)
    print(total)

main()