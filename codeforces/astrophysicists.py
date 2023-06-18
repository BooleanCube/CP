t = int(input())
for _ in range(t):
    n,k,g = map(int, input().split())
    tot = k*g
    s = g//2 if g&1 else g//2-1
    s *= n-1
    r = (tot-s)%g
    e = r if r<g/2 else r-g
    print(s+e if tot >= s else tot)
