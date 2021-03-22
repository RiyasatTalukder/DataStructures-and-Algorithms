"""
Given a string of capital letters and k allowed replacements,
the algorithm finds the longest repeating substring using k replacement
of characters.

Time: O(n)
Space: O(1)
"""
def characterReplacement(s, k):
    characters = [0]*26
    start, highest_frequency = 0, 0
    
    #sliding window technique
    for i in range(len(s)):
        characters[ord('A') - ord(s[i])]+=1
        highest_frequency = max(highest_frequency, characters[ord('A') - ord(s[i])])
        capacity = highest_frequency + k
        #if the window can no longer make k changes, shift the window
        if(capacity < i-start+1):
            characters[ord('A') - ord(s[start])]-=1
            start+=1
    #best window size
    return len(s) - start

assert characterReplacement("ABAAB", 2) == 5
assert characterReplacement("ABABABAA", 1) == 4
