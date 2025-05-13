#missing number in first n numbers  TC:O(n)     in operator TC:O(n)
nums=[1,2,3,5]
sum=0
n=5
f=n*(n+1)//2
for i in range(len(nums)):
    sum+=nums[i]
print(f-sum)
    

#missing number by range
nums=[1,2,4,5]
n=5
for i in range(1,n):
    if i not in nums:
        print(i)

  