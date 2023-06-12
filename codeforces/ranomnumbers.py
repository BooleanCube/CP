# WA on tc 9 because only accounts for "E" changes

t = int(input())
val = {"A":1, "B":10, "C":100, "D":1000, "E":10000}
for _ in range(t):
    s = input()
    if len(set(s))==1 and s[0] == "E":
        print(val["E"]*len(s))
        continue
    psum = [0]*(len(s))
    for i in range(1, len(s)):
        if not s[i-1] == "E":
            psum[i] = val[s[i-1]] + psum[i-1]
        else:
            psum[i] = -val[s[i-1]] + psum[i-1]
    ans = 0
    b = 0
    m = []
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        v = val[c]
        m.append(10000+ans-psum[i])
        cur = -v if v<b else v
        ans += cur
        b = max(b, cur)
    print(max(m))
