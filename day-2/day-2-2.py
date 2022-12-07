
def main():
    f = open("input", "r")
    total = 0
    """
    A = STEN 1
    B = PAPI 2
    C = SAKS 3
    X = LOSE
    Y = TIE
    Z = WIN
    LOSS = 0
    TIE  = 3
    WIN  = 6
    """
    points = {
        "A X" : 3,
        "A Y" : 4,
        "A Z" : 8,
        "B X" : 1,
        "B Y" : 5,
        "B Z" : 9,
        "C X" : 2,
        "C Y" : 6,
        "C Z" : 7,
    }

    for line in f:
        total += points[line[:3]]
        
    print(total)

main()