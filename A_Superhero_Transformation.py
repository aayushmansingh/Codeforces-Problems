s=input()
t=input()
l=['a','e','i','o','u']
if len(s)!=len(t):
    print("No")
    exit(0)
else:
    for i in range(len(s)):
        if s[i] in l and t[i] not in l:
            print("No")
            exit(0)
        elif s[i] not in l and t[i] in l:
            print("No")
            exit(0)
    else:
        print("Yes")