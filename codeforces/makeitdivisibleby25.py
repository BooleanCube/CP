t = int(input())
for z in range(t):
    n = input()
    l = len(n)
    s00,s25,s50,s75 = 20,20,20,20
    for i in range(l):
        s = n[i]
        ss = n[i+1:]
        zi = ss.find("0")
        fi = ss.find("5")
        if s == "0" and zi > -1: s00 = min(s00, l-zi+zi-i)
        elif s == "2" and fi > -1: s25 = min(s25, l-fi+fi-i)
        elif s == "5" and zi > -1: s50 = min(s50, l-zi+zi-i)
        elif s == "7" and fi > -1: s75 = min(s75, l-fi+fi-i)
    print(min(s00, s25, s50, s75)-2)
