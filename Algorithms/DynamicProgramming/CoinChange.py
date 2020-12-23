def coinChange(coins, amount):
    """
    Given the avialble coins, the algorithm finds 
    the minimum number of coins required to sum to
    the amount. If not possible, it returns -1. We 
    assume there a unlmited supply of coins.

    Time: O(nC)
    Space: O(C)
    """
    #dp apprach: The subproblems we are solving are the minimum number of coins required to form amount i
    #The base case is 0 as the minimum number of coins required to form 0 is 0
    #Therefore the recursive formula is:
    #   - dp[i] = min(dp[i-j]+1. dp[i]), if i >= current coin value

    dp = [float('inf')]*(amount + 1)
    dp[0] = 0
    
    for i in range(1, len(dp)):
        for j in coins:
            if(i >= j):
                dp[i] = min(dp[i-j]+1, dp[i])

    return dp[amount] if dp[amount] != float('inf') else -1

A = [1,2,5]
assert 3 == coinChange(A, 11)