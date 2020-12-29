def numDecodings(s):
    """
    Given a string of numbers, the algorithm decodes
    the string and returns the number of possible messages
    that can be decoded. The decoding is defined as:
    '1' -> 'A', '2' -> 'B' ..... '26' -> 'Z'

    Time: O(n)
    Space: O(n)
    """
    if(len(s) == 0):
        return 0
    #initialize dp array
    dp = [0 for _ in range(len(s)+1)]
    #base cases
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    #dp approach: we have the possibility of decoding 1 character or 2 characters
    #if we decide to decode 1 character, we add the number of ways to decode the i-1 charcters, if ith character is valid
    #Similarly, for 2 characters, we add the number of ways to decode the i-2 charcters, if i-2:i characters are valid
    #We add these together to account for both possibilities

    for i in range(2, len(dp)):
        if(int(s[i-1:i]) > 0):
            dp[i]+=dp[i-1]
        if(10 <= int(s[i-2:i]) <= 26):
            dp[i]+=dp[i-2]
    return dp[-1]

s = '11111'
assert 8 == numDecodings(s)

