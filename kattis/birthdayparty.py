def dfs(m, p):
    s = []
    v = set()
    s.append([0, set([0])])
    while len(s) > 0:
        x = s[-1]
        c = x[0]
        v = x[1]
        s.pop(-1)
        print(c,v,m[c])
        for ch in m[c]:
            if ch == 0 and len(v) == p: return False
            elif ch in v: continue
            s.append([ch, v.union(set([ch]))])
    return True

while 1:
    tc = input()
    if tc == "0 0": break
    p, c = map(int, tc.split())
    m = {}
    for i in range(p): m[i] = []
    for i in range(c):
        a, b = map(int, input().split())
        m[a].append(b)
        m[b].append(a)
    print("Yes" if c==1 or dfs(m, p) else "No")

