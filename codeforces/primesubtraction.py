t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    print("NO" if a==b+1 else "YES")
