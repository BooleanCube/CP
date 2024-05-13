from collections import Counter
n = int(input())
for _ in range(n): print(Counter(input()).most_common()[0][0])