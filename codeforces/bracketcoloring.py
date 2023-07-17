tc = int(input())
for _ in range(tc):
    n = int(input())
    b = input()
    path = []
    ns, rs = 0, 0
    for i in range(n):
        cur = b[i]
        if cur == "(":
            if rs > 0:
                rs -= 1
                path.append(2)
            else:
                ns += 1
                path.append(1)
        if cur == ")":
            if ns > 0:
                ns -= 1
                path.append(1)
            else:
                rs += 1
                path.append(2)
    if rs or ns:
        print(-1)
        continue
    else:
        print(len(set(path)))
        print(*([1]*n if len(set(path)) == 1 else path))

