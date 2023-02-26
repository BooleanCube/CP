t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    t1 = input()
    t2 = input()
    ts1 = sum(0 if t1[i]!=t1[i-1] else 1 for i in range(1, a))
    ts2 = sum(0 if t2[i]!=t2[i-1] else 1 for i in range(1, b))
    if ts1 + ts2 > 1:
        print("NO")
    elif ts1 + ts2 == 1 and t1[-1] == t2[-1]:
        print("NO")
    else:
        print("YES")
