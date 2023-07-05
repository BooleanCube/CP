t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    if x == 1 and k == 1:
        print("NO")
    elif x == 1 and n&1:
        if k == 2:
            print("NO")
        else:
            print("YES")
            print(n//2)
            print(" ".join("2"*(n//2-1)+"3"))
    elif x == 1:
        print("YES")
        print(n//2)
        print(" ".join("2"*(n//2)))
    else:
        print("YES")
        print(n)
        print(" ".join(list("1"*n)))
