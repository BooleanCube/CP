t = int(input())

for _ in range(t):
    a,b,c = map(int, input().split())
    print("YES" if a+b>9 or b+c>9 or a+c>9 else "NO")
