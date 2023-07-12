tc = int(input())
for _ in range(tc):
    a, b = map(int, input().split())
    print(1 if a>1 else a+b)
