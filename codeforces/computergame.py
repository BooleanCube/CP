t = int(input())
for _ in range(t):
    n = int(input())
    f = input()
    s = input()
    flag = True
    for i in range(n):
        if f[i]==s[i]=='1':
            flag = False
            print("NO")
            break
    if flag:
        print("YES")
