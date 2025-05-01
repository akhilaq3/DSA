def getpower(x,n):
    if n == 0:
        return 1
    # if power is odd we decrement the value of n and multiply with base 
    if n % 2 == 1:
        return x * getpower(x,n-1)
    #if power is even we perforn recursive call by passing x square and n//2 as parameters
    return getpower(x*x,n//2)
#main function execution starts here
def power(x,n):
    if n<0:
        x=1/x
    n=abs(n)
    return getpower(x,n)
#driver code
x=int(input())
n=int(input())
res=power(x,n)
print(res)