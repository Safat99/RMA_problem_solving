## this was for Amsa vai's proble...this was interesting...it's question is included in my
#whatsapp conversation with him...(for remembering where the problem is)

n = int(input())
print()
w = [input() for i in range(n)]
print()
t = input()

count = 0

for i in w:
    if i in t:
        count +=1

if count ==len(w):
    tmp = 1
else:
    tmp = 0

if tmp ==0:
    result = 'No'
    print(result)
    exit()

concat = ''
if tmp == 1:
    for i in w:
        concat +=i

for i in t:
    if i not in concat:
        result = 'No'
        break

result = 'Yes'
print(result)