#Problem Link: https://codeforces.com/problemset/problem/141/A

guest=input()
host=input()
result=input()
freq={}
for i in guest:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in host:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
freqres={}
for i in result:
    if i in freqres:
        freqres[i]+=1
    else:
        freqres[i]=1
if freq==freqres:
    print("YES")
else:
    print("NO")
