t = int(input())
for i in range(t):
    n=list(map(int,input().split(" ")))
    l=sorted(list(map(float,input().split(" "))))
    l=l[n[1]:len(l)-n[2]]
    print(sum(l)/len(l))
