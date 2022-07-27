t=int(input())
for i in range(t):
    input()
    text=input()
    cs=[]
    countc=0
    countt=0
    for i in text[::-1]:
        if i=='C':
            countc+=1
        cs.append(countc)
    cs = cs[::-1]
    for i in range(len(text)-1):
        if text[i]=='A':
            countt += cs[i+1]
    print(countt)
