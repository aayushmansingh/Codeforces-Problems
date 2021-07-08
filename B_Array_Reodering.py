import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    l = list(map(int, input().split()))
    even = []
    odd = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    final = []
    for i in range(len(even)):
        final.append(even[i])
    for j in range(len(odd)):
        final.append(odd[j])

    res = 0
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            if math.gcd(final[i], 2*final[j]) > 1:
                res += 1
    print(res)
