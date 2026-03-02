# n=5
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)


n=5
def fact(n):
    if n<=0:
        return 1
    return n*fact(n-1)
print(fact(n))