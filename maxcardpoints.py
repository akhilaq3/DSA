cardPoints=list(map(int,input().split()))
n=len(cardPoints)
k=int(input())
left=0
right=k-1
leftSum=sum(cardPoints[left:right+1])
rightSum=0
rightIndex=n-1
maxSum=leftSum
for i in range(k-1,-1,-1):
    leftSum-=cardPoints[i]
    rightSum+=cardPoints[rightIndex]
    maxSum=max(maxSum,leftSum+rightSum)
    rightIndex-=1
print(maxSum)