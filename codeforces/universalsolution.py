from collections import Counter

b = {"R":"P", "P":"S", "S":"R"}
n = int(input())

for _ in range(n):
    s = input()
    c = b[Counter(s).most_common()[0][0]]
    print(c*len(s))
