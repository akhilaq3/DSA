def generatesubset(ind,curr,ans,arr):
    if ind==len(arr):
        ans.append(curr.copy())
        return
    curr.append(arr[ind])
    #take part
    generatesubset(ind+1,curr,ans,arr)
    curr.pop()
    # dont take part
    generatesubset(ind+1,curr,ans,arr)
#main function
def subset(arr):
    ind=0
    curr=[]
    ans=[]
    generatesubset(ind,curr,ans,arr)
    return ans
#driver code
arr=list(map(int,input().split()))
res=subset(arr)
print(res)