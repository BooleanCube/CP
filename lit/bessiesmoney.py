from collections import defaultdict,Counter
from math import factorial as fac
n = int(input())
coin_denominations = list(map(int,input().split()))
fl = []
for i in range(5):
    fl.extend([i+1]*coin_denominations[i])
m = len(fl)

if m < 6:
    print(0)
    exit(0)

visited = set()
freqmp = Counter(fl)
count = 0
for a in range(m):
    freqmp[fl[a]] -= 1
    for b in range(a+1,m):
        freqmp[fl[b]] -= 1
        for c in range(b+1,m):
            freqmp[fl[c]] -= 1
            for d in range(c+1,m):
                freqmp[fl[d]] -= 1
                for e in range(d+1, m):
                    f = n-(fl[a]+fl[b]+fl[c]+fl[d]+fl[e])
                    freqmp[fl[e]] -= 1
                    if f in freqmp and freqmp[f]>0:
                        k = tuple(sorted([fl[a],fl[b],fl[c],fl[d],fl[e],f]))
                        if k in visited: freqmp[fl[e]] += 1; continue
                        freq = defaultdict(int)
                        freq[fl[a]] += 1
                        freq[fl[b]] += 1
                        freq[fl[c]] += 1
                        freq[fl[d]] += 1
                        freq[fl[e]] += 1
                        freq[f] += 1
                        divisor = 1
                        for b in freq.values():
                            divisor *= fac(b)
                        count += (fac(6) // divisor)
                        visited.add(k)
                    freqmp[fl[e]] += 1
                freqmp[fl[d]] += 1
            freqmp[fl[c]] += 1
        freqmp[fl[b]] += 1
    freqmp[fl[a]] += 1
                        
print(count)
