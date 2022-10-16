n,m = map(int,input().split())
c = 1
while True:
    c %= n+1
    if c>m: break
    m -= c
    c += 1
print(m)
