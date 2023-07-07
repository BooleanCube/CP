import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

def bs(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i+1
    return 1

t = int(input())
o = []
for _ in range(t):
    n,m,h = map(int, input().split())
    rud = list(map(int, input().split()))
    rud.sort()
    te = 0
    tes = 0
    idxt = 0
    while idxt < m:
        if tes+rud[idxt] > h:break
        te += tes+rud[idxt]
        tes += rud[idxt]
        idxt += 1
    p = [list(map(int, input().split())) for i in range(n-1)]
    res = [(-idxt,te)]
    for ppl in p:
        ppl.sort()
        s = 0
        p = 0
        idx = 0
        while idx < m:
            if s+ppl[idx] > h:break
            p += s + ppl[idx]
            s += ppl[idx]
            idx += 1
        res.append((-idx, p))
    res.sort()
    o.append(bs(res, (-idxt, te)))

print("\n".join(map(str,o)))
