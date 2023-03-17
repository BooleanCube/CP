n, k = map(int, input().split())
 
nums = list(range(1, n+1))
v = set()
current = k%n
ans = []
while len(ans) < len(nums):
    v.add(current)
    ans.append(nums[current])
    cnt = 0
    if len(ans) >= len(nums):
        break
    while cnt < 2*k:
        current += 1
        current %= n
        if current not in v:
            cnt += 1
print(" ".join (map(str, ans)))
