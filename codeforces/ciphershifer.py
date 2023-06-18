t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    c = s[0]
    o = ""
    i = 1
    while i < n:
        if s[i] == c:
            o += c
            if i < n-1:
                i += 1
                c = s[i]
        i += 1
    print(o)
