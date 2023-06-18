import math

t = int(input())
for _ in range(t):
    A,B,C,k = map(int, input().split())
    if C<A or C<B:
        print(-1)
        continue
    a = pow(10, A-1)
    c = 2*pow(10,A-1) if A==B==C else pow(10,C-1)
    b = c-a
    oa = a
    ob = b
    bb = pow(10,B-1)
    oc = c
    bc = pow(10,C-1)
    cf = pow(10,C)-1
    bf = pow(10,B)-1
    af = pow(10,A)-1
    k -= 1
    f = 1
    while k > 0:
        if b >= min(cf-a, bf):
            if a >= af:
                f = 0
                break
            else:
                a += 1
                b = max(bb, min(bf, bc-a))
                k -= 1
        else:
            u = min(k, cf-a-b, bf-b)
            k -= u
            b += u
    print(f"{a} + {b} = {a+b}" if f else -1)
