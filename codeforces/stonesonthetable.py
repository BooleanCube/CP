n = int(input())
counter = 0
s = list(input())
for i in range(n-1):
    if s[i]==s[i+1]:
        counter+=1
print(counter)
