for i in range(int(input())):
    l = int(input())
    a = list(map(int, input().split()))
    d = {}

    for i in range(l):
        if a[i] - i in d.keys():
            d[a[i] - i] += 1
        else:
            d[a[i] - i] = 1

    print(int(sum(i * (i - 1) / 2 for i in d.values())))
