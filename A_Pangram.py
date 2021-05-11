s = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
word = input().lower()
c = 0
if n < 26:
    print("NO")
    exit(0)
else:
    for i in s:
        if i not in word:
            print("NO")
            exit(0)

        else:
            pass
print("YES")
