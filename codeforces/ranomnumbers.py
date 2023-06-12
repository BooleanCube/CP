# WA on tc 9 because only accounts for "E" changes

t = int(input())
val = {"A":1, "B":10, "C":100, "D":1000, "E":10000}
for _ in range(t):
    s = input()
    if len(set(s))==1 and s[0] == "E":
        print(val["E"]*len(s))
        continue
    psuma = [0]*(len(s))
    psumb = [0]*(len(s))
    psumc = [0]*(len(s))
    psumd = [0]*(len(s))
    psume = [0]*(len(s))
    psum = [psuma, psumb, psumc, psumd, psume]
    let = "ABCDE"
    for i in range(1, len(s)):
        psuma[i] = val[s[i-1]] + psuma[i-1]
        if not s[i-1] >= "B":
            psumb[i] = val[s[i-1]] + psumb[i-1]
        else:
            psumb[i] = -val[s[i-1]] + psumb[i-1]
        if not s[i-1] >= "C":
            psumc[i] = val[s[i-1]] + psumc[i-1]
        else:
            psumc[i] = -val[s[i-1]] + psumc[i-1]
        if not s[i-1] >= "D":
            psumd[i] = val[s[i-1]] + psumd[i-1]
        else:
            psumd[i] = -val[s[i-1]] + psumd[i-1]
        if not s[i-1] == "E":
            psume[i] = val[s[i-1]] + psume[i-1]
        else:
            psume[i] = -val[s[i-1]] + psume[i-1]
    ans = 0
    b = 0
    m = []
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        v = val[c]
        cm = 0
        for j in range(5):
            if let[j] == c: continue
            cv = -val[let[j]] if val[let[j]]<b else val[let[j]]
            cm = max(cm, cv+ans-psum[j][i])
        m.append(cm)
        cur = -v if v<b else v
        ans += cur
        b = max(b, cur)
    print(max(m))
