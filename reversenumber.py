# reversing a positive integer
# n=123
# rev=0
# while n>0:
#     rem=n%10
#     rev=rev*10+rem
#     n//=10
# print(rev)



#reverseing for negitive integer
n=-123
sign=1
rev=0
if n<0:
    sign=-1
    n=abs(n)
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
print(sign*rev)