n = int(input())

for _ in range(n):
    a,b,c = map(int, input().split())
    print("+" if a+b==c else "-")
