x, n = map(int, input().split())
inp = list(map(int, input().split()))
l = [0] + sorted(inp) + [x]
m = 0
for i in range(1, n+2):
    m = max(l[i]-l[i-1], m)
print(m)
