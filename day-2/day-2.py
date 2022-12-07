
def main():
    f = open("input", "r")
    total = 0
    """
    A, X = STEN 1
    B, Y = PAPI 2
    C, Z = SAKS 3
    LOSS = 0
    TIE  = 3
    WIN  = 6
    """
    points = {
        "A X" : 4,
        "A Y" : 8,
        "A Z" : 3,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 7,
        "C Y" : 2,
        "C Z" : 6,
    }

    for line in f:
        total += points[line[:3]]
    
    print(total)

main()