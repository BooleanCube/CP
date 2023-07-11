tc = int(input())
for _ in range(tc):
    n = int(input())
    l = input()
    z = l.count("0")
    x = sum(1 for i in range(n//2+1) if l[i]!=l[-i-1])
    if x>0:
        print("DRAW" if x==1 and z==2 else "ALICE")
    else:
        print("ALICE" if z&1 and z!=1 else "BOB")
