elfs = [0]
def main():
    f = open("input", "r")
    counter = 0
    for line in f:
        if(line == "\n"):
            elfs.append(0)
            counter += 1
        else:
            elfs[counter] += int(line)
    f.close()

    elfs.sort(reverse=True)
    pik = sum(elfs[:3])
    print(pik)

main()