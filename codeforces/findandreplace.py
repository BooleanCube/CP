n = int(input())

for _ in range(n):
    input()
    s = input()
    first = {}
    for i in range(len(s)):
        c = s[i]
        if c not in first:
            first[c] = i
    flag = 1
    for i in range(len(s)):
        c = s[i]
        if (i-first[c])%2 != 0:
            print("no")
            flag = 0
            break
        first[c] = i

    if flag:
        print("yes")
