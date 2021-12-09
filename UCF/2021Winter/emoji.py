n = int(input())
for i in range(n):
	visited = []
	emoji = input()
	flag = True
	for c in emoji:
		if(visited.count(c) > 0):
			print("Nope")
			flag = False
			break
		else:
			visited.append(c)
	if flag:
		print("Emote away!")

	
