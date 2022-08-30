n=int(input())
for i in range(n):
    n,m=map(int,input().split())
    b = n%2
    print("Tonya" if b==m%2 else "Burenka")
