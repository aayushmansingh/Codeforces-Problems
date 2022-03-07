n = int(input())
l = list(map(int, input().split()))
team = [1, 2, 3]
res = min(l.count(1), l.count(2), l.count(3))
print(res)
for i in range(1, res+1):
    print(l.index(1)+1, l.index(2)+1, l.index(3)+1)
    l[l.index(1)] = 0
    l[l.index(2)] = 0
    l[l.index(3)] = 0
