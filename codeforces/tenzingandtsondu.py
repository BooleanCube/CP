t = int(input())
for _ in range(t):
    input()
    a = sum(list(map(int, input().split())))
    b = sum(list(map(int, input().split())))
    print("Tsondu" if a>b else "Tenzing" if a<b else "Draw")
