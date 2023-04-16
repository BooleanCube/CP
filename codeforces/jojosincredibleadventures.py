t = int(input())
while t:
    s = input()
    if len(set(s)) == 1 and s[0] == '1':
        print(len(s)**2)
        t -= 1
        continue
    c = 0
    for i in range(s.rfind('0')+1, len(s)):
        c += 1
    m = 0
    for a in s[:s.rfind('0')+1]:
        if a == '1':
            c += 1
        else:
            m = max(c, m)
            c = 0
    m = max(m, c)
    print(1 if m == 1 else max(0, 2*(m-1)))
    t -= 1
