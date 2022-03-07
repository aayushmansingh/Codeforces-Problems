n = int(input())
for tc in range(n):
    cats = int(input())
    for i in range(1, cats-2, 2):
        print(i+1, i, end=' ')
    if cats % 2 == 0:
        print(cats, cats-1, end=' ')
    else:
        print(cats, cats-2, cats-1, end=' ')
    print()
