n=int(input())
for i in range(n):
	s = input()
	print("".join([i for i in s if i.isalpha() or i.isdigit() or i==' ']))