def fun(d1,d2):
    if len(d1)!=len(d2):
        return "not anagram"
    for i in d1:
        if i not in d2:
            return "not anagram"
        if d1[i]!=d2[i]:
            return "not anagram"
    return "anagram"
s1="abc"
s2="acb"
d1={}
d2={}
for i in range(len(s1)):
    if s1[i] not in d1:
        d1[s1[i]]=1
    else:
        d1[s1[i]]+=1
for i in range(len(s2)):
    if s2[i] not in d2:
        d2[s2[i]]=1
    else:
        d2[s2[i]]+=1  
print(fun(d1,d2))
