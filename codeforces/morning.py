tc = int(input())
a = [1,2,3,4,5,6,7,8,9,0]
while tc:
    tc -= 1
    l = [1] + list(map(int, input()))
    ans = 0
    for i in range(1, len(l)):
        ans += 1 + abs(a.index(l[i]) - a.index(l[i-1]))
    print(ans)