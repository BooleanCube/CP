n, m = map(int, input().split())
l = list(map(int, input().split()))
v = [0]*n


def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))


def next(l, idx):
    if idx > -1:
        return set([clamp(1, l[idx]-1, m), clamp(1, l[idx], m), clamp(1, l[idx]+1, m)])
    return list(range(1, m+1))


def nextv(value):
    return set([clamp(1, value-1, m), clamp(1, value, m), clamp(1, value+1, m)])


def dfs(l, idx):
    value = 0
    if v[idx] or l[idx]:
        return 1
    stack = [(i, 0) for i in next(l, idx-1)]
    while len(stack) > 0:
        current = stack.pop(-1)
        cur = current[0]
        path = current[1]
        if idx+path+1 >= len(l):
            value += path+1
            continue
        v[idx+path] = 1
        path += 1
        if l[idx+path] == 0 and path == 0:
            for i in next(l, idx-1):
                stack.append((i, path))
        elif l[idx+path] == 0:
            for i in nextv(cur):
                node = (i, path)
                stack.append(node)
        elif abs(cur-l[idx+path]) < 2:
            value += 1
    return value


ans = 1
for i in range(len(l)):
    ans *= dfs(l, i)
    ans %= 1000000007

print(ans)
