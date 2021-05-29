n = int(input())
l = list(map(int, input().split()))
if sum(l) < 4:
    print(sum(l))
    exit(0)
if sum(l) % 4 == 0:
    print(sum(l) // 4)
    exit(0)
else:
    rem = sum(l) % 4
    print(sum(l) // 4 + rem)
