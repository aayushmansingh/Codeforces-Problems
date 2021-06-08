import math
test = 1
test = int(input())
freq={}
for tc in range((test)):
    # Write your code....
    s=input()
    if s not in freq:
        print("OK")
        freq[s]=1
    else:
        print(s+str(freq[s]))
        freq[s]+=1

