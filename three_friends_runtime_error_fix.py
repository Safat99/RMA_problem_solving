n = int(input())
count=0
inputs = []

while(count<n):
	pos = list(map(int,input().split()))
	pos = sorted(pos)
	inputs.append(pos)
	count +=1

for i in range(len(inputs)):	
	if inputs[i][0] == inputs[i][1] == inputs[i][2]:
		print(0)
		continue
	elif inputs[i][0] == inputs[i][1] != inputs[i][2]:
		if inputs[i][2] - inputs[i][1] == 1:
			inputs[i][2] -=1
		else:
			inputs[i][2] -=1
			inputs[i][1] +=1
			inputs[i][0] +=1
		
	elif inputs[i][1] == inputs[i][2] !=inputs[i][0]:
		if inputs[i][1] - inputs[i][0] == 1:
			inputs[i][0] +=1
		else:
			inputs[i][0] +=1
			inputs[i][1] -=1
			inputs[i][2] -=1
		
	else:
		inputs[i][0] +=1
		inputs[i][2] -=1
		
	distance = abs(inputs[i][0] - inputs[i][1]) + abs(inputs[i][0] - inputs[i][2]) + abs(inputs[i][1] - inputs[i][2])
	
	print(distance)

