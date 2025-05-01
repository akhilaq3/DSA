def getvalid(ind,curr,open,close,ans,n):
    if open>n:
        return
    #checks for vaid braces 
    if ind==2*n and open==close:
        ans.append(curr)
        return
    #recursion function call for open braces
    getvalid(ind+1,curr+"(",open+1,close,ans,n)
    if open>close:
        #recursion function call for open braces
        getvalid(ind+1,curr+")",open,close+1,ans,n)
#main function execution starts here
def valid(n):
    ind=0
    open=0
    close=0
    curr=""
    ans=[]
    getvalid(ind,curr,open,close,ans,n)
    return ans
#driver code
n=int(input())
res=valid(n)
print(res)
