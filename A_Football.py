#Problem Link: https://codeforces.com/problemset/problem/96/A

n=int(input())
l=[]
for i in range(n):
    score=input()
    l.append(score)
if len(l)==1:
    print(l[0])
    exit(0)
else:
    freq={}
    for item in l:
        if item not in freq:
            freq[item]=1
        else:
            freq[item]+=1
    maxkey = max(freq, key=freq.get)
    print(maxkey)
