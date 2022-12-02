t = int(input())
r = ""
for i in range(t):
    n,s = map(int,input().split())
    v = s*2/n
    if v%1!=0:print("IMPOSSIBLE");continue
    v = int(v)
    st = -1
    for j in range(1, v//2):
        if (v-j-j)/(n-1) % 1 == 0: st = j; break
    if st==-1:print("IMPOSSIBLE");continue
    d = (v-st-st)//(n-1)
    if d==0: print("IMPOSSIBLE");continue
    end = d*n
    r += " ".join(map(str,[st+j for j in range(0,end,d)])) + "\n"
    # i hate my life even more now and even more this time
print(r)
