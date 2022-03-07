import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    l = list(map(int, input().split()))
    if (l[1] > l[0]):
        l[1] = l[0]
    s = input()
    for i in range(l[1]):
        while('101' in s):
            s = s.replace('101', '121')
        s = s.replace('01', '11')
        s = s.replace('10', '11')
    s = s.replace('2', '0')
    print(s)
