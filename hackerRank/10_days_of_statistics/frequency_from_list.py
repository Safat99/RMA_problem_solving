
n=int(input())
given_nmbr=list(map(int,input().split()))

#dictionary method

freq = {}

for i in given_nmbr:
    if i not in freq:
        freq[i] =1
    else:
        freq[i] +=1

for i,j in freq.items():
    print(i,j)