i=int
t=input
n=i(t())
m=10**9+7
while n>0:a,b,c=map(i,t().split());print(pow(a,pow(b,c,m-1),m));n-=1
