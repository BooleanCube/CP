n, m = map(int, input().split())
c = int(input())
print((n*min(1000,c)) + m*max(0, c-1000))
