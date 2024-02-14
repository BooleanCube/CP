tc = int(input())
while tc:
    tc -= 1
    a,b,c = map(int,input().split())
    a,b,c = sorted([a,b,c])
    print(c if a==b else a)