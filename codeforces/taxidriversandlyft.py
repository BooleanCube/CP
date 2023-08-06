from bisect import bisect_left

n, m = map(int, input().split())
citizens = list(map(int, input().split()))
riders, drivers = [], []
caste = list(map(int, input().split()))
for i in range(n+m):
    if caste[i]: drivers.append(citizens[i])
    else: riders.append(citizens[i])
drivers.sort()
taxis = {pos:0 for pos in drivers}
for rider in riders:
    idx = bisect_left(drivers, rider)-1
    if idx < 0: taxis[drivers[0]] += 1
    elif idx >= len(drivers)-1: taxis[drivers[idx]] += 1
    elif abs(drivers[idx]-rider) <= abs(drivers[idx+1]-rider): taxis[drivers[idx]] += 1
    else: taxis[drivers[idx+1]] += 1
print(*[taxis[key] for key in sorted(taxis.keys())])
