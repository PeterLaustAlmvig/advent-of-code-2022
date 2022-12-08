import copy
def checkRow(forest, copy):
    total = 0
    for i in range(len(forest)):
        running_max = -1
        count = 0
        #Check row from the left
        for j in range(len(forest[i])):
            if(forest[i][j] > running_max):
                if(copy[i][j] != -1):
                    total += 1
                    running_max = forest[i][j]
                    copy[i][j] = -1
                    count = len(forest[i][:j])+1
                    if(running_max == 9):
                        break
            
        #Check row from the right
        running_max = -1
        for j in range(len(forest[i])-count):
            if(forest[i][len(forest[i])-j-1] > running_max):
                if(copy[i][len(forest[i])-j-1] != -1):
                    total += 1
                    running_max = forest[i][len(forest[i])-j-1]
                    copy[i][len(forest[i])-j-1] = -1
                    if(running_max == 9):
                        break
    return total

def checkColumn(forest, copy):
    total = 0
    for i in range(len(forest)):
        running_max = -1
        count = 0
        
        #Check column from top
        for j in range(len(forest[i])):
            if(forest[j][i] > running_max):
                if(copy[j][i] != -1):
                    total += 1
                    running_max = forest[j][i]
                    copy[j][i] = -1
                    count = len(forest[:j])+1
                    if(running_max == 9):
                        break
                else:
                    running_max = forest[j][i]
            
        #Check column from bottom
        running_max = -1
        for j in range(len(forest[i])-count):
            if(forest[len(forest[i])-j-1][i] > running_max):
                if(copy[len(forest[i])-j-1][i] != -1):
                    total += 1
                    running_max = forest[len(forest[i])-j-1][i]
                    copy[len(forest[i])-j-1][i] = -1
                    if(running_max == 9):
                        break
                else:
                    running_max = forest[len(forest[i])-j-1][i]
    return total
            
def main():
    forest = list()
    for line in open("day-8/input", "r"):
        row = [int(x) for x in line.strip()]
        forest.append(row)
    copy = [x[:] for x in forest]

    tot1 = checkRow(forest, copy)
    print("Total across: ", tot1)
    tot2 = checkColumn(forest, copy)
    print("Total up/down:", tot2)
    print("Total total: ", tot1+tot2)

main()