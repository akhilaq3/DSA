# n=int(input("enter"))
# a=0
# b=1
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c)





# n=int(input())
# a,b=0,1
# while a<n: 
#     print(a)
#     a,b=b,a+b

# n=3
# a,b=0,1
# for _ in range(n):
#     a,b=b,a+b
# print(a)



def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(3))
