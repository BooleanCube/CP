import random as r
 
n = 5000
ops = ["I [num]", "R", "M"]
inp = "I 57820"
val = 1
for i in range(n):
    num = r.randint(-10e6, 10e6)
    idx = r.randrange(3)
    if val > 0:
        inp += "/" + ops[idx].replace("[num]", str(num))
    else:
        inp += "/I " + str(num)
    if idx==0: val += 1
    if idx==1: val -= 1
out = ""
l = []
for op in inp.split("/"):
    if op[:1] == "I":
        l.append(int(op.split()[1]))
        l.sort()
    elif op=="R":
        out += str(l.pop(0)) + "/"
    else:
        out += str(l[0]) + "/"
print(len(inp))
print(inp)
print(out[:-1])
