import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n = int(input())
    if (int((n/2)**0.5) == (n/2)**0.5) or (int((n/4)**0.5) == (n/4)**0.5):
        print("YES")
    else:
        print("NO")
