t = int(input())
for z in range(t):
    n, s = input().split()
    n = int(n)
    l = (input()*2)[::-1]
    d = -1
    li = -1
    #print(l)
    for i in range(n*2):
        if l[i] == "g": li = i
        #print(l[i], s, li, i, i-li, d)
        if l[i] == s and i>=n: d = max(d, i-li)
    print(d)

