l = [0]
for i in range(1, 10**6):
    l.append(l[-1] + sum(int(c) for c in str(i)))

tc = int(input())
while tc:
    tc -= 1
    print(l[int(input())])