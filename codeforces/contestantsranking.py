from collections import defaultdict

tc = int(input())
for _ in range(tc):
    n = int(input())
    teams = [input().split() for _ in range(n)]
    ppl = defaultdict(lambda : 1e20)
    ppl["Ahmad"] = 0
    updated = 1
    while updated:
        updated = 0
        for team in teams:
            best = ""
            bestrank = 1e21
            for i in range(3):
                if ppl[team[i]] < bestrank:
                    best = team[i]
                    bestrank = ppl[team[i]]
            for person in team:
                if ppl[person] > bestrank+1:
                    ppl[person] = bestrank+1
                    updated = 1
    ans = [(ppl[key], key) for key in ppl]
    ans.sort()
    print(len(ans))
    for a,b in ans:
        print(b,("undefined" if a == 1e20 else a))
