def LCIS(arr1, n, arr2, m):
    table=[0]*m
    for j in range(m): table[j]=0
    for i in range(n):
        current = 0
        for j in range(m):         
            if (arr1[i] == arr2[j]):
                if (current+1 > table[j]): table[j] = current+1
            if (arr1[i] > arr2[j]):
                if (table[j] > current): current = table[j]
    return max(table)

t = int(input())
for m in range(t):
    n=int(input())
    l=list(map(int, input().split(" ")))
    a=2*LCIS(l,n,l[::-1],n)-1
    print(a)
