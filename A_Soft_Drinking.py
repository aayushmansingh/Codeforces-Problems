n, k, l, c, d, p, nl, np = map(int, input().split())
soda = (k*l)//nl
lime = (c*d)
salt = (p//np)
print(min(soda, salt, lime)//n)
