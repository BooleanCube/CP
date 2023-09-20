from itertools import combinations
t = int(input())
for _ in range(t):
    b,k = map(int, input().split())
    bags = [set(list(map(int, input().split()))[1:]) for _ in range(b)]
    ans = 0
    for comb in combinations(bags, k):
        cur = set()
        for s in comb: cur = cur.union(s)
        ans = max(ans, len(cur))
    print(ans)
