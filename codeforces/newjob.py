def ceil(a, b):
    return a//b + int(a%b>0)

tc = int(input())
for _ in range(tc):
    steps, opened = 0, 1
    n, m = map(int, input().split())
    n += 1
    done = 0
    while opened < m:
        opened *= 2
        steps += 1
        if opened >= n:
            done = 1
            break
    if done: print(steps)
    else: print(steps + ceil(n-opened, m))