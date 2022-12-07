def main():
    total = 0
    for line in open("input", "r"):
        x, y, z, w = map(int, line.strip().replace(",", "-").split("-"))
        if((x <= z and y >= w) or (z <= x and w >= y)):
            total += 1
    
    print(total)

main()