def solve(n, l):
    if n<3 or len([c for c in l if c>0]) == 0:
        return max(l)
    return max(sum(c for c in l[0:n:2] if c>0), sum(c for c in l[1:n:2] if c>0))

tc = int(input())
for _ in range(tc):
    n = int(input())
    l = list(map(int, input().split()))
    print(solve(n, l))

