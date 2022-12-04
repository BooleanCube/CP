def twoSum(nums, target):
    required = {}
    for i in range(len(nums)):
        if target - nums[i] in required:
            return True
        else:
            required[nums[i]]=i
    return False

n = int(input())
for z in range(n):
    n,s = map(int, input().split())
    l = sorted(list(map(int, input().split())),reverse=True)
    if n == 1:
        if l[0]%s == 0: print(l[0]//s)
        else: print(0)
        continue
    st = (l[0]+l[1])//s * s
    et = l[-1]+l[-2]
    c = st+s
    ans = True
    while c>=et:
        if twoSum(l,c):print(c//s);ans=False;break
        c -= s
    if ans:
        for y in l:
            if y%s==0:print(y//s);ans=False;break
    if ans:print(0)
