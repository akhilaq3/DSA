#generation of subsets whose sum equal to target 
def generate(ind,curr,ans,candidates,target):
    if target==0:
        ans.append(curr.copy())
        return
    if target<0 or ind==len(candidates):
        return
    curr.append(candidates[ind])
    #take part
    generate(ind,curr,ans,candidates,target-candidates[ind])
    curr.pop()
    #dont take part
    generate(ind+1,curr,ans,candidates,target)
#execution starts here
def combination(candidates,target):
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,candidates,target)
    return ans
#Driver code
candidates=list(map(int,input().split()))
target=int(input())
res=combination(candidates,target)  
print(res)      