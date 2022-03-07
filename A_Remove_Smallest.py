for i in range(int(input())):
    n = input()
    l = sorted(list(map(int, input().split())))
    a = l[0]
    for j in l[1::]:
        if j == a or j == (a+1):
            a = j
        else:
            print("NO")
            break
    else:
        print("YES")
