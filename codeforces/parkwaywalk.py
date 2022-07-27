i=input
t=int(i())
for j in range(t):
    n,m=map(int,i().split())
    s=sum(map(int,i().split()))
    print(s-m if s>m else 0)
