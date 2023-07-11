n, k = map(int, input().split())
l = list(map(int, input().split()))
if k == 1:
    print(max(l))
    print(n)
    exit(0)
l = sorted([(val, idx) for idx,val in zip(range(n), l)], reverse=True)
s, o = sum(x[0] for x in l[:k]), sorted([x[1] for x in l[:k]])
p = o[0]+1
ans = [p]
for i in range(1, k-1):
    ans.append(o[i]+1-p)
    p = o[i]+1
if k > 1:
    ans.append(n-p)
print(s)
print(*ans)
