ans = 0
n, m = map(int, input().split())
ans += n+n//(m-1)
if n % (m-1) == 0:
    ans -= 1
print(ans)
