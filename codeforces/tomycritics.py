for _ in range(int(input())):
    a,b,c = map(int, input().split())
    print("yes" if a+b>9 or b+c>9 or a+c>9 else "no")
