#Problem Link: https://codeforces.com/problemset/problem/732/A

n, k = map(int, input().split())
c = 0
prod = n
i = 1
while (n % 10 not in [0, k]):
    i += 1
    n = i * prod
print(i)
