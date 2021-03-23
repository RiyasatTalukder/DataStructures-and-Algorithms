"""
Given a list of stock prices, the algorithm finds the max 
profit a trader can make. However, once you sell a stock,
you have a 1 day cooldown before you can buy again.

Time: O(n)
Space: O(n)
"""

def maxProfit(prices):
    #initialize dp array
    dp = [[0]*2 for _ in range(len(prices))]
    #base cases
    #dp[i][0] represents cash (sell)
    #dp[i][1] represents hold stock (buy)
    dp[0][0], dp[0][1] = 0, -prices[0]
    
    #dp[i][0] represents the max profit on the ith day
    for i in range(1, len(prices)):
        #Either I hold my cash from yesterday, or I sell my stock
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #Either I hod my stock from yesterday, or I buy a stock using cash from 2 days ago
        #i-2 because there is 1 day cool period so I need to get the cash from selling 2 days ago
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    
    #last day represents the max profit over all days
    return dp[-1][0]

assert maxProfit([1,2,3,0,2]) == 3
assert maxProfit([1,2,3,0,2,8]) == 9