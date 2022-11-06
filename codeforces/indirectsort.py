t = int(input())
for z in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    print("YES" if min(l) == l[0] else "NO")
