i=input
n,q=map(int,i().split())
l=[0]
for j in sorted(map(int,i().split()),reverse=True):
    l.append(j)
p=[]
s=0
for j in l:
    s+=j
    p.append(s)
r=[]
for j in range(q):
    x,y=map(int,i().split())
    r.append(p[x]-p[x-y])
print("\n".join(map(str,r)))
