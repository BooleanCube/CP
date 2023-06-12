t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    idx = 0
    max = 1
    while abs(l[idx]-1-idx) == 0:
        idx += 1
    max = abs(l[idx]-1-idx)
    for i in range(idx+1, n):
        num = l[i]
        cur = abs(num-1-i)
        if cur == 0 or cur%max == 0:
            continue
        elif max%cur == 0:
            max = cur
        else:
            max = 1
    print(max)
