tc = int(input())
while tc:
    tc -= 1
    for _ in range(3):
        l = input()
        if "?" in l:
            print("A" if "A" not in l else "B" if "B" not in l else "C")
