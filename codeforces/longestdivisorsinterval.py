for _ in range(int(input())):
    n = int(input())
    a = 1
    while n%a == 0:
        a += 1
    print(a-1)
