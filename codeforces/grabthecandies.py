n = int(input())

for _ in range(n):
    input()
    l = list(map(int, input().split()))
    e = sum(i for i in l if i&1==0)
    o= sum(i for i in l if i&1)
    print("yes" if e>o else "no")
