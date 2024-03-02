import sys
from collections import OrderedDict

input = sys.stdin.readline
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")

for _ in range(int(input())):
    n = int(input())
    a, b, c, d = OrderedDict(), OrderedDict(), OrderedDict(), OrderedDict()
    ans = 0
    for i in range(1, n+1):
        x, y = map(int, input().split())
        va = a[x] if x in a else 0
        vb = b[y] if y in b else 0
        vc = c[x+y] if x+y in c else 0
        vd = d[x-y] if x-y in d else 0
        ans += va + vb + vc + vd
        a[x] = va+1
        b[y] = vb+1
        c[x+y] = vc+1
        d[x-y] = vd+1
    print(ans << 1)
