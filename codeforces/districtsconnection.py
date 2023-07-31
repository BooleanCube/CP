t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if len(set(l)) == 1:
        print("NO")
        continue
    ops = []
    val = l[0]
    idx = [i for i in range(len(l)) if l[i] != val][0]
    for i in range(1, len(l)):
        if l[i] != val: ops.append([1, i+1])
        else: ops.append([i+1, idx+1])
    print("YES")
    for op in ops:
        print(*op)
