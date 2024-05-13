k = int(input())

fq = [1]*10

idx, p = 0, 1
while p < k:
    p //= fq[idx]
    fq[idx] += 1
    p *= fq[idx]
    idx += 1
    idx %= 10

s = "codeforces"
ans = ""
for i in range(len(s)):
    ans += s[i]*fq[i]
print(ans)