s = input()
ans = 0
v = set()
for c in s:
    if c in v: v.remove(c)
    else: ans += len(v); v.add(c)
print(ans)
