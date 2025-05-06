
def maxProfit(prices):
    maxprofit=0
    n=len(prices)
    minvalue=prices[0]
    for i in range(n):
        maxprofit=max(maxprofit,prices[i]-minvalue)
        minvalue=min(minvalue,prices[i])           
    return maxprofit
#buy and sell
prices=list(map(int,input().split()))
res=maxProfit(prices)
print(res)

      