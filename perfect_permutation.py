n = int(input())

if n % 2 != 0:
	output = -1
	print(output)
else:
	output = []
	for i in range(1,n+1):
		if i%2==1:
			output.append(i+1)
		else:
			output.append(i-1)
	print(" ".join(str(x) for x in output))
