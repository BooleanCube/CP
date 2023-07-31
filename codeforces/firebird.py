n, k = map(int, input().split())
l = list(map(int, input().split()))
for i in range(1, n):
    if l[i] >-1:
        j = i
        while j>0 and l[j]>0 and l[j-1]==-1:
            l[j-1] = l[j]-1
            j -= 1
for i in range(1, n):
    if l[i-1] >= k-1 and l[i] == -1:
        l[i] = 0
    elif -1 < l[i-1] < k-1:
        l[i] = l[i-1]+1
    if l[i] > -1 and i < n-1 and l[i+1] == 0:
        j = i
        while l[j] < k-1:
            l[j] += k
            j -= 1
ans = l.count(0)
print(ans)
