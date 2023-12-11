n = int(input())
l = list(map(int, input().split()))
print(sum(l)+max(0, max(l)-sum(l)))
