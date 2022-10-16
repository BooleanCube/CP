twopn = [2**i for i in range(33)]
#print(twopn)
t = int(input())
for z in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    twoc = 0
    for i in l:
        for j in range(32, 0, -1):
            #print(i, j, twopn[j])
            if i%twopn[j]==0:twoc += j;break
    #print(twoc)
    if twoc >= n: print(0);continue
    m = {}
    for i in range(2,n+1):
        for j in range(32, 0, -1):
            if i%twopn[j]==0:
                if j not in m: m[j] = [i];break
                m[j].append(i);break
    #print(m)
    c = 0
    for i in sorted(m.keys(), reverse=True):
        if twoc >= n: break
        for x in m[i]:
            if twoc>=n: break
            twoc += i
            c+=1
    #print(twoc, n)
    print(-1 if n>twoc else c)
