t=int(input())
l=[]
for i in range(t//2):
    a=input()
    b=input()
    r=a+"-"+b if a<=b else b+"-"+a
    l.append(r)
print(" ".join(l[::-1]))
