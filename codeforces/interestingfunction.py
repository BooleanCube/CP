import math

m = {}
m[1] = 1
for i in range(1,11):
    a = 10**i
    m[a] = a+m[10**(i-1)]


pows={
    0:1,
    1:10,
    2:100,
    3:1000,
    4:10000,
    5:100000,
    6:1000000,
    7:10000000,
    8:100000000,
    9:1000000000,
    10:10000000000
}

def func(n):
    for i in range(10,-1,-1):
        if n>=pows[i] and n%pows[i]==0: return pows[i]
    return 1

def countn(n):
    c = 0
    while True:
        if n%10 == 9: c+=1;n//=10
        else: return c

n = int(input())
for i in range(n):
    s,e=map(int,input().split())
    counter = 0
    while s<e:
        #print(s,e,a)
        a = func(s)
        counter += m[a]+countn(s//a)
        s += a
        if s > e:
            e-=s
            s=0
            continue

    print(counter)
