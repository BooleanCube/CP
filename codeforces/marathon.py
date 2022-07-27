t = int(input())
for i in range(t):
    l = list(map(int,input().split()))
    print(sum(1 for j in l if j>l[0]))
