import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

o = []

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    nidx = ([i for i in range(n-1, 0, -1) if a[i] < 0] + [-1])[0]
    ops, ops2 = [], []
    for i in range(nidx, 0, -1):
        while a[i] < a[i-1]:
            ops.append([i, i+1])
            a[i-1] += a[i]
    for i in range(nidx+1, n-1):
        while a[i+1] < a[i]:
            ops.append([i+2, i+1])
            a[i+1] += a[i]
    o.append(str(len(ops)))
    for op in ops:
        o.append(f"{op[0]} {op[1]}")

print("\n".join(o))
