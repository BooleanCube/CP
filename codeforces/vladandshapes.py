tc = int(input())
while tc:
    tc -= 1
    n = int(input())
    l = set()
    for _ in range(n):
        l.add(input().count("1"))
    print("SQUARE" if len(l) <= 2 else "TRIANGLE")