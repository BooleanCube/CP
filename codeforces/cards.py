from functools import cache

ans = ""

@cache
def backtrack(r, g, b):
    global ans
    if r+g+b == 2:
        if 2 in [r,g,b]:
            ans += "RGB"[[r,g,b].index(2)]
            return 1
        else:
            ans += "RGB"[[r,g,b].index(0)]
            return 1
    if r > 1: backtrack(r-1, g, b)
    if g > 1: backtrack(r, g-1, b)
    if b > 1: backtrack(r, g, b-1)
    if r>0 and g>0: backtrack(r-1, g-1, b+1)
    if g>0 and b>0: backtrack(r+1, g-1, b-1)
    if r>0 and b>0: backtrack(r-1, g+1, b-1)
 

n = int(input())
rgb = input()
if len(rgb) == 1:
    print(rgb)
    exit(0)
backtrack(rgb.count("R"), rgb.count("G"), rgb.count("B"))
print("".join(sorted(map(str, set(ans)))))
