from collections import Counter
n, k = map(int, input().split())
l = list(map(int, input().split()))
f, l = Counter(l), sorted(set(l))
s = sum(f[l[i]] for i in range(len(l)-1) if 0 < l[i+1]-l[i] <= k)
print(n-s)
