n=input()
def bool(s):
    for i in range(len(s)):
        if s[i]!='1' and s[i]!='4':
            return False
    if s[0]!='1':
        return False
    if s.find('444')!=-1:
        return False
    return True
if bool(n):
    print("YES")
else:
    print("NO")