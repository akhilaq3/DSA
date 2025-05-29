#Brute force approach Time Complexity O(N**2)
nums=list(map(int,input().split()))
target=int(input())
n=len(nums)
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            print([i,j])


#if the list is sorted then we use two pointer technique Time complexity O(Nlogn)
nums=list(map(int,input().split()))
target=int(input())
nums.sort()
n=len(nums)
low=0
right=n-1
while low<=right:
    if nums[low]+nums[right]==target:
        print([low,right])
        break
    elif nums[low]+nums[right]<target:
        low+=1
    else:
        right-=1


#using hashing Time complexity O(N)
nums=list(map(int,input().split()))
target=int(input())
n=len(nums)
d={}
for a in range(n):
    b=target-nums[a]
    if b in d:
        print([d[b],a])
    else:
        #storing list values along with indexes in dictionary
        d[nums[a]]=a 