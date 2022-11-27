n = int(input())
for i in range(n):
    s,a = input().split()
    v = int(a) if s=="D" else int(a,8) if s=="O" else int(a,2) if s=="B" else int(a,16)
    print(v, hex(v)[2:], oct(v)[2:], bin(v)[2:])
