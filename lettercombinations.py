 #generating letter combinations of a phone number
def lettercombo(ind,curr,ans,combos,digits):
    #if no digits given then empty list will be returned
    if len(digits)==0:
        return []
    #appending actual combinations
    if ind==len(digits):
        ans.append(curr)
        return
    #accessing digits
    i=int(digits[ind])
    #generating combinations by using recursion call
    for j in combos[i]:
        lettercombo(ind+1,curr+j,ans,combos,digits) 
#execution starts here
def lettercombination(digits):
    ind=0
    curr=""
    ans=[]
    combos=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    lettercombo(ind,curr,ans,combos,digits)
    return ans
#driver code
digits=input()
res=lettercombination(digits)
print(res)       