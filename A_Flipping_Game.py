n = int(input())
l = list(map(int, input().split()))
c0 = 0
c1 = 0
temp = n
s = 0
for i in l:
    if i:
        c0 -= 1
        c0 = max(c0, 0)
        c1 += 1
    else:
        c0 += 1
        s = max(c0, s)
if c1 == temp:
    print(temp - 1)
else:
    print(s + c1)
