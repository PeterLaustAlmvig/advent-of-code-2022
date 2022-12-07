from collections import Counter
Counter()

total = 0
def main():
    f = open("input", "r")
    line = f.readline()
    while line:
        part1 = line.strip("\n")
        part2 = f.readline().strip("\n")
        part3 = f.readline().strip("\n")
        checkLetter(part1, part2, part3)
        line = f.readline()

    print(total)


def checkLetter(part1, part2, part3):
    global total
    for letter in part1:
            if(letter in part2 and letter in part3):
                if(letter.islower()):
                    total += ord(letter)-96
                else:
                    total += ord(letter)-38
                
                return

main()