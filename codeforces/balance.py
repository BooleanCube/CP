def kmex(l, k):
    for i in range(1, len(l) + 2):
        if k * i not in l: k * i
    return k * (len(l) + 3)


q = int(input())
s = set()
for z in range(q):
    t = input().split()
    if t[0] == "+": s.add(int(t[1]))
    else: print(kmex(s, int(t[1])))
