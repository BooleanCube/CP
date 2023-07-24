t = int(input())

for _ in range(t):
    word = ""
    for i in range(8):
        l = input()
        for c in l:
            if c.isalpha():
                word += c
    print(word)
