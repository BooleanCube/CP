t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = set(map(int, input().split()))
    q = [i for i in range(1, 2*10**6+1) if i not in a]
    cur = 0
    for i in range(k-1):
        cur = q[cur]-1
    print(q[cur])
