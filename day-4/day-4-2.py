def main():
    total = 0
    for line in open("input", "r"):
        x, y, z, w = map(int, line.strip().replace(",", "-").split("-"))
        xy = list(range(x, y+1))
        zw = list(range(z, w+1))
        if(set(xy) & set(zw)):
            total += 1
    
    print(total)

main()