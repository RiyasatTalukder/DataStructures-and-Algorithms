def numDecodings(s):
    if(len(s) == 0):
        return 0
    if(len(s) == 1):
        return 1 if s[0] != '0' else 0
    if('00' in s[:2]):
        return 0
    
    dp = [0 for i in range(len(s)+1)]
    dp[1] = 1 if s[0] != '0' else 0
    dp[2] = 2 if '0' not in s[:2] and int(s[:2]) <= 26 else 1
    
    for i in range(3, len(dp)):
        if(s[i-1] != '0'):
            dp[i] = dp[i-1] + dp[i-2]
    
    print(dp)
    return dp[-1]
    