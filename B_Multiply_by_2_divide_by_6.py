import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    if n == 1:
        print(0)
        continue
    count_2 = 0
    while n % 2 == 0:
        count_2 += 1
        n = n // 2
    count_3 = 0
    while n % 3 == 0:
        count_3 += 1
        n //= 3
    if n == 1 and count_3 >= count_2:
        print(2 * count_3 - count_2)
    else:
        print(-1)