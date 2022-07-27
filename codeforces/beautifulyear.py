n = int(input())+1
findingDistinct = True
while findingDistinct:
    s = str(n)
    ad = True
    for c in s:
        if s.count(c) > 1:
            ad = False
            break
    if ad:
        print(n)
        findingDistinct = False
        break
    n+=1
