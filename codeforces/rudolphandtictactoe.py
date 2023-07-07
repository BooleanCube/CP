import sys

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")


o = []
t = int(input())
for _ in range(t):
    d = 0
    b = [input() for _ in range(3)]
    for i in range(3):
        if len(set(b[i].strip())) == 1:
            if b[i][0] == ".": continue
            o.append(b[i][0] if not b[i][0] == "." else "DRAW")
            d = 1
            break
        if len(set([b[j][i] for j in range(3)])) == 1:
            if b[0][i] == ".": continue
            o.append(b[0][i] if not b[0][i] == "." else "DRAW")
            d = 1
            break
    if d: continue
    if len(set(b[i][i] for i in range(3))) == 1 and not b[0][0] == ".":
        o.append(b[0][0] if not b[0][0] == "." else "DRAW")
        d = 1
    if not d and len(set(b[i][-i-2] for i in range(3))) == 1 and not b[0][-2] == ".":
        o.append(b[0][-2] if not b[0][-2] == "." else "DRAW")
        d = 1
    if not d:
        o.append("DRAW")

print("\n".join(o))
