n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

final = []
for i in range(max(a),min(b)+1):
	final.append(i)
	
	
print(len(final))
