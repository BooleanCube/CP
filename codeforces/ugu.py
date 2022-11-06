t = int(input())
for z in range(t):
    input()
    s = input()
    p = -1
    prev = -11234525000000
    if s[0] == '0': p -= 1;prev = 0
    for i in range(len(s)):
        if s[i] != prev: p += 1
        prev = s[i]
    print(max(0,p))
