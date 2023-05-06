t = int(input())
for _ in range(t):
    n = int(input())
    books = {0:[], 1:[], 2:[]}
    for i in range(n):
        b, m = input().split()
        if m == "11":
            books[2].append(b)
        elif m == "10":
            books[0].append(b)
        elif m == "01":
            books[1].append(b)
    for k in books:
        books[k] = sorted(list(map(int, books[k])))
    if len(books[2])==0 and (len(books[0])==0 or len(books[1])==0):
        print(-1)
    else:
        if len(books[0])==0 or len(books[1])==0: print(books[2][0])
        elif len(books[2]) == 0: print(books[1][0]+books[0][0])
        else: print(min(books[2][0], books[0][0]+books[1][0]))
