t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    psum = [0]*(n+1)
    for i in range(1, n+1):
        psum[i] = l[i-1] + psum[i-1]
    s = 0
    e = n-1
    lo = s
    hi = lo+(e-s)//2
    while e>s:
        print("? " + str(hi-lo+1) + " " + " ".join(map(str,range(lo+1, hi+2))))
        esum = psum[hi+1]-psum[lo]
        rsum = int(input())
        if rsum > esum:
            e = hi
            hi = lo+(e-s)//2
        else:
            s = hi+1
            lo = s
            hi = lo+(e-s)//2
    print("! " + str(e+1)) 
