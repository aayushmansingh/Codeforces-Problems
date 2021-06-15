#Problem Link: https://codeforces.com/problemset/problem/466/A 

n, m, a, b = map(int, input().split())
cost = 0
if m * a <= b:
    print(n * a)
else:
    if n > m:
        cost += (n // m) * b
        n -= (n // m) * m
        if n * a < b:
            cost += n * a
        else:
            cost += b
        print(cost)
    else:
        cost = min(n * a, b)
        print(cost)
