s="aBcfGh"
res=""
for i in range(len(s)):
    if s[i]>='a' and s[i]<='z':
        res+=chr(ord(s[i])-32)
    else:
        res+=chr(ord(s[i])+32)
print(res)
