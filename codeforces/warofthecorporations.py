ai = input()
p = input()
c = 0
i = 0
while i < len(ai)-len(p)+1:
    if ai[i:i+len(p)] == p:
        c += 1
        i += len(p) - 1
    i += 1
print(c)
