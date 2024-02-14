from math import log2

def msb(n):
    for i in range(5): n |= (n >> (1 << i))
    n += 1
    return (n >> 1)

tc = int(input())

while tc:
    tc -= 1
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        d = l[i-1] - l[i]
        if d > 0:
            s = int(log2(msb(d)))+1
            l[i] = l[i-1]
            ans = max(ans, s)
    print(ans)