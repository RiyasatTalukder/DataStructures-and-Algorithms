"""
Given a string, the algorithm counts all the 
substrings that are palindromes.

Time: O(n^2)
Space: O(1)
"""

def countSubstrings(s):
    palindromes = 0
    
    #count palindromes in a sub string
    def countPalindromes(s, left, right):
        count = 0
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left-=1
            right+=1
            count+=1
        return count
    
    #go through all the sub strings 
    for i in range (len(s)):
        #even palindrome
        palindromes+=countPalindromes(s,i,i)
        #odd palindrome
        palindromes+=countPalindromes(s,i,i+1)
    
    return palindromes

assert countSubstrings("bbbb") == 7
assert countSubstrings("bbracecar") == 13