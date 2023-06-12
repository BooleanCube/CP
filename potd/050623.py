ans = []
for a in range(1, 18):
    for b in range(a, 18):
        for c in range(1, 18):
            for d in range(c, 18):
                if a**3+b**3 == c**3+d**3 and (a,b) != (c,d) and (a,b) != (d,c):
                    ans.append((a**3+b**3, a, b, c, d))
print(min(ans))
