n = int(input())
c = 0
for i in range(n):
    if input().count("1") > 1:
        c+=1
print(c)
