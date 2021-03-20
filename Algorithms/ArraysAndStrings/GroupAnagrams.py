"""
Given a list of words (size m), the algorithm finds
all the anagrams associated with each word and returns
them.

Time: O(n*mlogm)
Space: O(n*m)
"""
def groupAnagrams(strs):
    words = {}
    for i in strs:
        curr_word = tuple(sorted(i))
        #add anagram to the associated word
        if curr_word in words:
            words[curr_word].append(i)
        else:
            words[curr_word] = [i]
    
    return [i for i in words.values()]

assert groupAnagrams(["eat", "tea", "tan"]) == [["eat", "tea"], ["tan"]]