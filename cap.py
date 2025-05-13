s="abceik"
res=""
for i in range(len(s)):
    if s[i] in "aeiou":
        res+=chr(ord(s[i])-32)
    else:
        res+=s[i]
print(res)