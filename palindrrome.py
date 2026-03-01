# n=input("enter")
# ncopy=n
# if n==ncopy[::-1]:
#     print("yes")
# else:
#     print("no")

#PALINDROME OTIMISED
# s=input()
# m=len(s)
# n=len(s)//2
# palindrome=True
# for i in range(n):
#     l=s[i]
#     r=s[m-1-i]
#     if l!=r:
#         palindrome=False
#         break
# if palindrome:
#     print("YES")
# else:
#     print("NO")

#printing name number times
# name=input()
# number=int(input())
# print(name*number)


# for i in range(number):
#     print(name)




#TABLE
# def table(n):
#     for i in range(1,11):
# #         print(str(n) + "*" + str(i) + "=" + str(n*i))
# #         print(n,"*",i,"=",n*i)
#           print(f"{n} * {i} = {n*i}")
# table(5)


# def even(n):
#     for i in range(1,n+1):
#         if i%2==0:
#            print(i)
# even(10)

#SUM OF ELEMENTS IN A LIST
#l=[2,8,6,5,4]
# summ=0
# for i in l:
#       summ+=i
# print(summ)
#print(sum(l))


#SUM OF ABSOLUTE DIFFERENCE OF ASCII VALUES OF ADJACENT CHARACTERS IN A STRING
# s=input()
# score=0
# for i in range(len(s)-1):
#     a=ord(s[i])
#     b=ord(s[i+1])
#     temp=abs(a-b)
#     score+=temp
# print(score)
# print(ord("v"),ord("n"),ord("i"))

# arr=[10,50,25,36,90,80]
# print(max(arr))
# maximum=0
# for i in range(len(arr)):
#     if maximum<arr[i]:
#         maximum=arr[i]
# print(maximum)
# for i in arr:
#     if maximum<i:
#        maximum=i
# print(maximum)



#PRINTING FIRST ROW AND COLUMN ELEMENTS
# tarr=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(tarr)):
#     for j in range(len(tarr[i])):
#         print(tarr[i][0])
#         break


# arr=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(tarr)):
#     for j in range(len(tarr[i])):
#         print(tarr[0][j])
#     break



# r=3
# c=12
# for i in range(r):
#     for j in range(c):
#         print("*",end="")
#         if j!=c-1:
#             print("-",end="")
#     print()


# r=20
# c=3
# for i in range(r):
#     for j in range(c):
#         print("*",end="")
#         if j!=c-1:
#             print("-",end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end="")
#         else:
#               if j!=n-1:                       #to avoid space at the end of pattern
#                print(" ",end="")
#     print()
# n=3
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()



# r=5
# c=4
# for i in range(r):
#     for j in range(r-i):
#         print(" ",end="")
#     for k in range(c):
#         print("*",end="")
#     print()
# r=5
# c=4
# for i in range(r):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(c):
#         print("*",end="")
#     print()


n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for k in range(i+1):
        if j==n:
            continue
        print("*",end="")
    
    print()