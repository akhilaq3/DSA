#generating sunsets whose sum is equal to target 
def generate(ind,curr,ans,candidates,target):
    if target==0:
        ans.append(curr.copy())
        return
    if target<0 or ind==len(candidates):
        return
    curr.append(candidates[ind])
    generate(ind+1,curr,ans,candidates,target-candidates[ind])
    curr.pop()
    #subset combinations are not repeated
    for i in range(ind+1,len(candidates)):
        if candidates[ind]!=candidates[i]:
            generate(i,curr,ans,candidates,target)
            break
#execution starts here
def combination(candidates,target):
    candidates.sort()
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,candidates,target)
    return ans
#driver code
candidates=list(map(int,input().split()))
target=int(input())
res=combination(candidates,target)
print(res)        