t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    c = min(s)
    p = s.rfind(c)
    if p > 0:
        print(c + s[:p] + s[p+1:])
    else:
        print(s)
