import math
d = int(input())
for z in range(d):
    n = int(input())
    ai = list(map(int, input().split()))
    m = int(input())
    bj = list(map(int, input().split()))
    alice = sum(pow(2,math.sqrt(c)) for c in ai)
    bob = sum(pow(2,math.sqrt(c)) for c in bj)
    print(alice,bob)
    print("Tie!" if alice==bob else "Alice will have more fun!" if alice>bob else "Bob will have more fun!")
