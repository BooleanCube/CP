def timetomin(s):
    h,m=map(int,s.split(":"))
    return h*60+m
def mintotime(m):
    return str((m//60)%24).zfill(2)+":"+str(m%60).zfill(2)

t=int(input())
for i in range(t):
    st,sc=input().split()
    c=int(sc)
    ps=[]
    if st==st[::-1]: ps.append(st)
    ct = mintotime(timetomin(st)+c)
    while ct!=st:
        if ct==ct[::-1]:ps.append(ct)
        ct = mintotime(timetomin(ct)+c)
    print(len(set(ps)))
