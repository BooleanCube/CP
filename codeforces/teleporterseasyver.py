
def solve():
    n, c = map(int, input().split())
    l = list(map(int, input().split()))
    for i in range(1, n+1): l[i-1] += i
    l.sort()
    s = 0
    for i in range(n):
        s += l[i]
        if s > c:
            print(i)
            break
    if s <= c:
        print(n)


t = int(input())
while t:
    solve()
    t -= 1
