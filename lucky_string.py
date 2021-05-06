inputs = int(input())
repeat = 'abcd'


result1 = inputs // 4 
extra1 = inputs % 4
if extra1 == 3 : repeat2 = 'abc'
elif extra1 == 2 : repeat2 = 'ab'
elif extra1 == 1 : repeat2 = 'a'

if extra1 ==0:
	final_result = repeat * result1
else:
	final_result = repeat * result1 + repeat2
print(final_result)
