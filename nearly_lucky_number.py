input_number = list(input())
counter = []

for i in input_number:
	if i=='4' or i=='7':
		counter.append(i)

lucky_finder = list(str(len(counter)))
lucky_counter = []

for i in lucky_finder:
	if i == '4' or i=='7':
		lucky_counter.append(i)

if len(lucky_counter) == len(lucky_finder):
	print('YES')
else:
	print('NO')
