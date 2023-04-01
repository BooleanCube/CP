t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    open = {}
    count = 0
    for i in range(len(l)):
        c = l[i]
        if c in open:
            open[c].append(i)
        else:
            open[c] = [i]
        if c+1 in open and len(open[c+1]) > 0:
            open[c+1].pop(-1)
        else:
            count += 1
    print(count)
