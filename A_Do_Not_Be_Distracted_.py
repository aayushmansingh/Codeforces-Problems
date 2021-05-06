import math
test = 1
test = int(input())

for tc in range((test)):
    # Write your code....
    n=int(input())
    string=input()
    freq=[0]*26
    alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(string)):
        if i not in freq:
            freq