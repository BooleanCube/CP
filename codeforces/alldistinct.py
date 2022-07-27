t=int(input())
for i in range(t):
    input()
    l=list(map(int,input().split()))
    while True:
        d=-1
        di=0
        for j in range(len(l)):
            if l.count(l[j])>1 and d==-1:
                d=1
                di=j
            elif l.count(l[j])>1:
                l.remove(l[j])
                l.remove(l[di])
                break
        if d==-1: break
    print(len(l))
