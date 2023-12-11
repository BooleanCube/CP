c=1
print(len([c:=a for a,b in sorted(list(map(int,input().split()))[::-1]for _ in"."*int(input()))if b>=c]))