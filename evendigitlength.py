nums=list(map(int,input().split()))
count=0
for i in nums:
    if len(str(i))%2==0:
        count+=1
print(count)

        