def main():
    total = 14
    f = open("input", "r")
    line = f.readline()
    chars = list()
    for i in range(14):
        chars.append(line[i])

    for char in line[14:]:
        if(len(chars) == len(set(chars))):
            print(total)
            return
        
        chars.pop(0)
        chars.append(char)
        total += 1
    
main()