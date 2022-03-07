s = input()
flag = 97
rot = 0
for i in range(len(s)):
    diff = abs(flag-ord(s[i]))
    if diff > 13:
        diff = 26-diff
    rot += diff
    flag = ord(s[i])
print(rot)
