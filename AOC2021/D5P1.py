nums = []
count = 0
for i in range(500):
	sin = input().split(" -> ")
	x1 = int(sin[0].split(",")[0])
	y1 = int(sin[0].split(",")[1])
	x2 = int(sin[1].split(",")[0])
	y2 = int(sin[1].split(",")[1])
	if y1 == y2:
		for i in range(len(nums)):
			si = nums[i].split(",")
			sx1 = int(si[0])
			sy1 = int(si[1])
			sx2 = int(si[2])
			sy2 = int(si[3])
			if ((sy1>=y1>=sy2 or sy1<=y1<=sy2) and (sx1>=x1>=sx2 or sx1<=x1<=sx2)) or ((sy1>=y2>=sy2 or sy1<=y2<=sy2) and (sx1>=x2>=sx2 or sx1<=x2<=sx2)):
				count+=1		
	elif x1 == x2:
		for i in range(len(nums)):
			si = nums[i].split(",")
			sx1 = int(si[0])
			sy1 = int(si[1])
			sx2 = int(si[2])
			sy2 = int(si[3])
			if ((sy1>=y1>=sy2 or sy1<=y1<=sy2) and (sx1>=x1>=sx2 or sx1<=x1<=sx2)) or ((sy1>=y2>=sy2 or sy1<=y2<=sy2) and (sx1>=x2>=sx2 or sx1<=x2<=sx2)):
				count+=1
	nums.append(str(x1)+","+str(y1)+","+str(x2)+","+str(y2))
print(count)
