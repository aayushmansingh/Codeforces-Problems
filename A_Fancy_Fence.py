#Problem Link: https://codeforces.com/problemset/problem/270/A

import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    a=int(input())
    print("YES" if (360%(180-a)==0) else "NO")
