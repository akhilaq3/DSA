# string multiplication for the given string consisting of a digit followed by a character(every 2nd index is digit rest characters)
s="3a4d5c"
n=len(s)
res=""
for i in range(0,n,2):
    res+=int(s[i])*s[i+1]
print(res)
  

#multiple digits and single character
s="21a8n7i"
res=""
num=""
for i in range(len(s)):
    if ord(s[i])>=48 and ord(s[i])<=57:
        num+=s[i]
    else:
        res+=int(num)*s[i]
        num=""
print(res)

#string multiplication when we have multiple integers and multiple characters
s="11abc1h"
res=""
num=""
alpha=""
for i in range(len(s)):
    if ord(s[i])>=48 and ord(s[i])<=57:
        num+=s[i]
    else:
        alpha+=s[i]
        if i+1==len(s) or ord(s[i+1])>=48 and ord(s[i+1])<=57:
            res+=int(num)*alpha
            num=""
            alpha=""
print(res)