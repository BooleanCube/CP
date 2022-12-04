t = int(input())
for z in range(t):
    n,m = map(int, input().split())
    ol = set()
    nl = set()
    for i in range(m):
        x = sorted(list(map(int, input().split())))
        if x[0] == 1: ol.add(x[1])
        if x[-1] == n: nl.add(x[0])
    i = ol.intersection(nl)
    print(len(i))
    for j in list(i):
        print(j)
    #if z != t-1:
    print()
