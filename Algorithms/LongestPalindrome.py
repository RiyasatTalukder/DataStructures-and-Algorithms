def longestPalindrome(s: str):
    """
    Given a string, the algorithm finds the longest substring
    palindrome within the string and returns its length.

    Time: O(n^2)
    Space: O(n^2)
    """
    start = 0
    end = 0

    #DP Approach: The subproblems to solve is checking if S[i:j] is a palindrome
    #Two conditons for valid palindrome: 
    # 1) S[i] == S[j] (the start and end has to be same for palindrome)
    # 2) DP[i+1][j-1] is a palindrome (the string between, S[i+1][j-1], also has to be plaindrome)

    dp = [[False]*len(s) for i in range(len(s))]
    
    #a string itself is palindrome
    for i in range(len(s)):
        dp[i][i] = True
    
    #strings of length 2 
    for i in range(len(s)-1):
        if(s[i] == s[i+1]):
            dp[i][i+1] = True
            start = i
            end = i+1
    
    #rest of the substrings
    for i in range(2, len(s)):
        k = 0
        j = i
        while(k < len(s)-i):
            if(s[k] == s[j] and dp[k+1][j-1]):
                dp[k][j] = True
                if(end-start < j-k):
                    start = k
                    end = j
            j+=1
            k+=1
    
    return s[start:end+1]

s = "aabbaaracecar"
print(longestPalindrome(s))