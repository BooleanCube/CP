def next(n, x):
    x += 1
    return x-n if x>n else x


n, m = map(int, input().split())
l = list(map(int, input().split()))
s = 0
for i in range(1, m):
    f = next(n, l[i-1])
    diff = 0
    if f == l[i]: diff = 0
    elif f < l[i]: diff = min(l[i]-f, f+n-l[i])
    else: diff = min(f-l[i], l[i]+n-f)
    s += diff
print(s)
