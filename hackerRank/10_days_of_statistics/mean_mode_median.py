# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
given_nmbr=list(map(int,input().split()))
given_nmbr.sort()
#avrg
mean=sum(given_nmbr)/len(given_nmbr)
print(mean)
#median
if len(given_nmbr)%2==0:
    median=(given_nmbr[int(len(given_nmbr)/2)]+given_nmbr[int((len(given_nmbr)/2)-1)])/2
    print(median)
else:
    median=given_nmbr[int((len(given_nmbr)+1)/2)-1]
    print(median)
#mode
unique_nmbr=[]
final=[]
for i in given_nmbr:
    if i not in unique_nmbr:
        unique_nmbr.append(i)
counter=[0]*len(unique_nmbr)
for i in given_nmbr:
    for j in range(len(unique_nmbr)):
        if i == unique_nmbr[j]:
            counter[j]+=1
#print(counter)
for i in range(len(unique_nmbr)):
    if counter[i]==max(counter):
        final.append(unique_nmbr[i])

mode=final[0]
print(mode)


'''
results
Input(stdin)
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Expected Output
43900.6
44627.5
4978

'''
