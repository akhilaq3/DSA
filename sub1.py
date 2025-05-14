s="3a4d5c"
n=len(s)
res=""
for i in range(0,n,2):
    res+=int(s[i])*s[i+1]
print(res)
  