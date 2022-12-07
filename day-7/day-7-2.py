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
candidates = list()
###############
    
def SumTree(root):
    if(len(root.childs) != 0):
        for child in root.childs:
            SumTree(child)
        for child in root.childs:
                root.increase(child.size)

def find_folder(root, space_needed):
    global candidates
    if(root.size >= space_needed):
        candidates.append(root.size)
    for child in root.childs:
        find_folder(child, space_needed)
    
def SumTree(root):
    if(len(root.childs) != 0):
        for child in root.childs:
            SumTree(child)
        for child in root.childs:
                root.increase(child.size)

def main():
    global total
    global candidates
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
    print(root.size)
    total_space = 70000000
    used = root.size
    space_left = total_space - used
    space_needed = 30000000 - space_left
    find_folder(root, space_needed)
    print(min(candidates))

main()