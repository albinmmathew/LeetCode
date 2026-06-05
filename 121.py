# Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        dp[0]=-prices[0]
        m=dp[0]
        for i in range(1,len(prices)):
            dp[i]=max(m+prices[i],-prices[i])
            if dp[i]<=0:
                m=max(m,-prices[i])
        print(dp)
        if max(dp)<0:
            return 0
        else:
            return max(dp)