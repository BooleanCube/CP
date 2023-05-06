t = int(input())
for i in range(t):
    s = input()
    c = 0
    for j in range(10):
        c += 1 if "codeforces"[j] != s[j] else 0
    print(c)
