for _ in range(int(input())):
    ans = ""
    for i in range(8):
        ans += "".join([c for c in input() if c.isalpha()])
    print(ans)
