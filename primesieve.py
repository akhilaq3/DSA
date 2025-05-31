n=int(input())

dup=[1]*n
for i in range(2,n):
    if dup[i]==1:
        for j in range(i*i,n,i):
            dup[j]=0
count=0
for k in range(2,n):
    if dup[k]==1:
        count+=1
print(count)
    

