import re
def main():
    supply = [["T", "P", "Z", "C", "S", "L", "Q", "N"],
    ["L", "P", "T", "V", "H", "C", "G"],
    ["D", "C", "Z", "F"],
    ["G", "W", "T", "D", "L", "M", "V", "C"],
    ["P", "W", "C"],
    ["P", "F", "J", "D", "C", "T", "S", "Z"],
    ["V", "W", "G", "B", "D"],
    ["N", "J", "S", "Q", "H", "W"],
    ["R", "C", "Q", "F", "S", "L", "V"]]
    
    f = open("input", "r")
    for i in range(10):
        f.readline()

    for line in f:
        x = re.findall(r'\d+', line)
        #print(x[2])
        popped = []
        for j in range(int(x[0])):
            popped.append(supply[int(x[1])-1].pop())
        
        popped.reverse()
        for i in range(len(popped)):
            supply[int(x[2])-1].append(popped[i])
            

    for inner in supply:
        print(inner[-1])
main()