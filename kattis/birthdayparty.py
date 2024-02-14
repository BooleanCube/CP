from collections import defaultdict

def dfs(m, p):
    s = []
    v = set()
    s.append(0)
    while s:
        x = s.pop(-1)
        c = x
        if c in v: continue
        v.add(c)
        for ch in m[c]:
            if ch in v: continue
            s.append(ch)
    return len(v) == p

while 1:
    p, c = map(int, input().split())
    if p==0 and c==0: break
    freq = [0]*p
    vis = set()
    for i in range(c):
        a, b = map(int, input().split())
        if (a,b) in vis: continue
        vis.add((a,b)); vis.add((b,a))
        freq[a] += 1
        freq[b] += 1
    m = defaultdict(list)
    for pair in vis:
        a,b = pair
        m[a].append(b)
    if p==1:
        print("Yes")
        continue
    print("Yes" if any(freq[i] < 2 for i in range(p)) and dfs(m, p) else "No")
