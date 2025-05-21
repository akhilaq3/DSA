def binarysearch(nums,target):
    low=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return False
    
nums=list(map(int,input().split()))
target=int(input())
print(binarysearch(nums,target))