for _ in range(int(input())):
    n = int(input())
    mxb, mxi = 0, 0
    for i in range(n):
        a,b = map(int, input().split())
        if a<=10 and b > mxb: mxb, mxi = b, i+1
    print(mxi)
