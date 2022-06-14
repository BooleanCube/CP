n=int(input())
for i in range(n):
	t=input().split(",")
	name = t[0]
	sh=0;sm=0
	for i in range(1, 6):
		sh+=int(t[i].split(":")[0])
		sm+=int(t[i].split(":")[1])
	sh+=sm//60
	sm%=60
	h = str(sh)+" hours" if sh!=1 else str(sh)+" hour"
	if sm==0:
		m=""
	else:
		m = " "+ str(sm)+" minutes" if sm != 1 else " "+str(sm)+" minute"
	print(name+"="+h+m)
