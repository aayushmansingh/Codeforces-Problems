def solve(n):
    p = len(str(n))
    ans = (p - 1) * 9
    i = 1
    c = str(i)*p
    while True:
        if int(c) <= n:
            ans += 1
            i += 1
            c = str(i) * p
        else:
            return ans


for _ in range(int(input())):
    n = int(input())
    print(solve(n))