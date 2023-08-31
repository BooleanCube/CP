a, b = input().split()
if a==b: print(1);exit(0)
flag = 1
if len(a)==len(b):
    for i in range(len(a)):
        o = ord(a[i])
        adj = [o, o-1, o+1, o+8, o+9, o+10, o-8, o-9, o-10]
        if ord(b[i]) not in adj: flag = 0
else: flag=0
print(2 if flag else 3)
