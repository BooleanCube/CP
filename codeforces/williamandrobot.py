import sys
from queue import PriorityQueue

input = sys.stdin.readline
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")

n = int(input())
l = list(map(int, input().split()))
pq = PriorityQueue(); pq.put(max(l[:2]))
for i in range(2, n, 2):
    pq.put(l[i])
    if pq.queue[0] < l[i+1]:
        pq.get()
        pq.put(l[i+1])
ans = 0
while pq.queue: ans += pq.get()
print(ans)