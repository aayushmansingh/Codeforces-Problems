from itertools import permutations
import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    s=input()
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    if freq['T']==2*freq['M'] and s.index('T')<s.index('M'):
        print("YES")
    else:
        print("NO")
