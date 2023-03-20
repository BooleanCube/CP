import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(x)
    
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    l = list(map(int, input().split()))
    psum = [0]*(n+1)
    for i in range(1, n+1):
        psum[i] = l[i-1] + psum[i-1]
    ts = psum[-1]-psum[0]
    for i in range(q):
        s,e,k = map(int, input().split())
        r = e-s+1
        if (ts-psum[e]-psum[s-1])&1:
            print("no\n" if (k*r)&1 else "yes\n")
        else:
            print("no\n" if (k*r)&1==0 else "yes\n")
