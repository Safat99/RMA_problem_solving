n = int(input())
count=0
while(count<n):
	initial_positions = list(map(int,input().split()))
	sorted_pos = sorted(initial_positions)
	c=1
	#for i in range(len(sorted_pos)-1):
	for i in range(2):
		if sorted_pos[i] == sorted_pos[i+1]:
			c+=1
	if c!=1:
		if c==3:
			distance=0
			print(distance)
			continue
		else:
			if sorted_pos[0] == sorted_pos[1]:
				sorted_pos[2] -=1
			else:
				sorted_pos[0] +=1
	else:
		sorted_pos[0] +=1
		sorted_pos[2] -=1
	distance = abs(sorted_pos[0] - sorted_pos[1]) + abs(sorted_pos[0] - sorted_pos[2]) + abs(sorted_pos[1] - sorted_pos[2])
	print(distance)
	count +=1
