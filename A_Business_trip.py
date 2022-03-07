n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
res = 0
for i in l:
    if n < 1:
        break
    n -= i
    res += 1
if n > 0:
    res = -1
print(res)
