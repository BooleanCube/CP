from queue import PriorityQueue

n, k = map(int, input().split())
b = bin(n)[2:][::-1]
pq = PriorityQueue()
for i in range(len(b)):
    if b[i] == "1":
        pq.put(-(1 << i))
if len(pq.queue) > k:
    print("NO")
    exit(0)
while len(pq.queue) < k:
    c = -pq.get()
    if c == 1:
        print("NO")
        exit(0)
    pq.put(-(c>>1)); pq.put(-(c>>1))
print("YES")
print(*map(lambda x: -x, pq.queue))
