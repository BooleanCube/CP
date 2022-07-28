n,k = map(int, input().split())
ks = k**2
c = 0
for i in range(1,n+1):
    if i%k==0 and i%ks!=0: c+=1
print(c)
