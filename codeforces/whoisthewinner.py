tc = int(input())
for _ in range(tc):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    a = h1*3600+m1*60+s1
    b = h2*3600+m2*60+s2
    print("Tie" if a == b else "Player1" if a < b else "Player2")