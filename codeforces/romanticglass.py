import sys

input = sys.stdin.readline
print = lambda *args: sys.stdout.write(" ".join(map(str, args)) + "\n")

tc = int(input())
while tc:
    tc -= 1
    n = int(input())
    l = list(map(int, input().split()))
    l = [-l[i] if i&1 else l[i] for i in range(n)]
    psum = [0]
    for i in range(n): psum.append(psum[i]+l[i])
    print("YES" if len(set(psum)) < len(psum) else "NO")