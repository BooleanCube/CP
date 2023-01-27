n, m = map(int, input().split())
l = list(map(int, input().split()))
p = 1
if l[0] == 0 and l[1]>1: p*=3
elif l[0] == 0: p*=2
elif l[-1] == 0 and l[-2]<m: p*=3
elif l[-1] == 0: p*=2
for i in range(1, n-1):
    if l[i] != 0: continue
    a = l[i-1]
    b = l[i+1]
    d = abs(b-a)
    if d==1: p*=2
    elif d==0 and (a==1 or a==m): p*=2
    elif d==0: p*=3
print(p)
