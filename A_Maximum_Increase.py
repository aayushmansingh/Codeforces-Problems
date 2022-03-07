n = int(input())
l = list(map(int, input().split()))
c = 1
m = 1
for i in range(1, n):
    if l[i] > l[i-1]:
        c += 1
    else:
        m = max(m, c)
        c = 1
print(max(m, c))
