def checkSumSetK(ind,arr,k):
    if k==0:
        return True
    if k<0 or ind==len(arr):
        return False
    path1=checkSumSetK(ind+1,arr,k-arr[ind])
    if path1==True:
       return True
    path2=checkSumSetK(ind+1,arr,k)
    return path1 or path2

def subset(arr,k):
    ind=0
    res=checkSumSetK(ind,arr,k)
    return res
    

#driver code
arr=list(map(int,input().split()))
k=int(input())
print(subset(arr,k))