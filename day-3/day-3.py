total = 0
def main():
    f = open("input", "r")
    for line in f:
        part1 = line[:len(line)//2]
        part2 = line[(len(line)//2):-1]
        checkLetter(part1, part2)
    print(total)


def checkLetter(part1, part2):
    global total
    for letter in part1:
            if(letter in part2):
                if(letter.islower()):
                    total += ord(letter)-96
                else:
                    total += ord(letter)-38
                
                return

main()