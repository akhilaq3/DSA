# n=int(input("enter number"))
# f=0
# for i in range(1,n):            #sum of divisors is equal to n
#     if(n%i)==0:
#         f=f+i
# if f==n:
#     print("perfect")
# else:
#     print("not perfect")



n=28
res=1
def perfect(n):
    res=1
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            res+=i
            if i!=n//i:
                res+=n//i
    if res==n:
        return True
    return False
print(perfect(n))
    
