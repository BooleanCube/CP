t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    freq = {i:0 for i in range(101)}
    for i in l:
        freq[i] += 1
    f = 1
    for i in set(l):
        if i>0 and freq[i] > freq[i-1]:
            f = 0
            break
    print("YES" if f else "NO")
