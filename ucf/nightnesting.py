a,b= map(int,input().split())
m = a%b
r = a//b
if m>0: r += 1
print(r)
