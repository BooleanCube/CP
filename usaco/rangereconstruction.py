n = int(input())
b = [[-69, -96] for i in range(1)]*(n+1)
b[1] = [0]
s = 0
diff = 0
done = 0
for i in range(1, n+1):
    l = list(map(int, input().split()))
    cmx = -1
    rmn = b[i][0]
    rmx = b[i][0]
    for j in range(1, len(l)):
        if l[j] > cmx:
            cmx = l[j]
            if len(b[i+j-1]) > 1:
                b[i+j] = [rmx-l[j], rmn+l[j]]
                break
            else:
                #print(i, j, l, b, rmn, rmx)
                v = rmn + l[j]
                p = b[i+j]
                if len(p) == 1: continue
                if p[0]!=-69 and p[1]!=-96 and v>p[1]: v = rmx - l[j]
                b[i+j] = [v]
                if v > 1000000000: diff = 1000000000
                rmn = min(rmn, v)
                rmx = max(rmx, v)
                s += 1
                if s == n:
                    done=1
                    break
        else:
            b[i+j] = [rmn, rmx]
    if done: break
print(*[b[i][0]-diff for i in range(1,n+1)])
