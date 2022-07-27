t=int(input())
for i in range(t):
    n,s=map(int, input().split())
    l=list(map(int, input().split()))
    if sum(l)<s:
        print(-1)
        continue
    if(sum(l)==s):
        print(0)
        continue
    
