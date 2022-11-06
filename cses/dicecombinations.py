n = int(input())
m = {}
for i in range(7): m[i+1] = 2**i
for i in range(7,n+1): m[i] = sum(m[i-j] for j in range(1,7))%(10**9+7)
print(m[n])
