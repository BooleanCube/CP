t=int(input())
for z in range(t):
    x,y=map(int,input().split())
    if x==3 and y==3:print(2,2)
    elif x==3 and y==2:print(2,2)
    elif y==3 and x==2:print(2,2)
    else:print(x,y)
