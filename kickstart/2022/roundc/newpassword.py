n=int(input())
for i in range(n):
    input()
    t=input()
    a=b=c=d=False
    for i in t:
        if i.isupper(): a=True
        if i.islower(): b=True
        if i.isdigit(): c=True
        if i in "#@*&": d=True
    if not a: t+="A"
    if not b: t+="a"
    if not c: t+="1"
    if not d: t+="*"
    if len(t)<7: t+="*"*(7-len(t))
    print(t)
