def lower(nums,target,n):
    low=0
    high=n-1
    ind=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ind=mid
            high=mid-1
        else:
            low=mid+1
    return ind
def upper(nums,target,n):
    low=0
    high=n-1
    while (low<=high):
        mid=(low+high)//2
        if nums[mid]>target:
            ind=mid
            high=mid-1
        else:
            low=mid+1
    return ind

nums=list(map(int,input().split()))
target=int(input())
n=len(nums)
lowerbound=lower(nums,target,n)
upperbound=upper(nums,target,n)-1
print(lowerbound,upperbound)