n = int(input())
l = list(map(int, input().split()))
lp, ls, rp, rs = 0, l[0], n-1, l[-1]
ans = 0
while lp < rp:
    if ls < rs:
        lp += 1
        ls += l[lp]
    elif ls > rs:
        rp -= 1
        rs += l[rp]
    else:
        ans = max(ans, ls)
        if l[lp+1]<l[rp-1]:
            lp += 1
            ls += l[lp]
        else:
            rp -= 1
            rs += l[rp]
        continue


print(ans)
