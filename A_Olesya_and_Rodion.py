n, t = map(int, input().split())
if n >= 2 and t == 10:
    for i in range(1, n):
        print(1, end="")
    print(0)
elif n == 1 and t == 10:
    print(-1)
else:
    for i in range(1, n + 1):
        print(t, end="")
