max = 0
pos=0
for i in range(5):
    l=map(int, input().split(" "))
    s = sum(l)
    if max<s:
        max=s
        pos=i+1
print(pos, max)
