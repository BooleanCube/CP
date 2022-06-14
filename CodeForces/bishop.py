t=int(input())
for i in range(t):
    input()
    m=[]
    for j in range(8):m.append(list(input()))
    for x in range(1,7):
        for y in range(1,7):
            if m[x-1][y-1]=="#" and m[x-1][y+1]=="#" and m[x+1][y-1]=="#" and m[x+1][y+1]=="#" and m[x][y] == "#":
                   print(x+1,y+1)

