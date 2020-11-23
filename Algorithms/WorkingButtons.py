def possibleWords(digits, words):
    """
    Given a phone with some working digits, determine if it possible to 
    construct the words with the working digits.

    Time: O(n+m)
    SpaceK O(n+m)
    """

    result = [False]*len(words)
    if(len(digits) == 10):
        return result
    
    digitString = {1:"", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz", 0:""}
    possible = ""
    for i in digits:
        possible+=digitString[i]
    for i in range(len(words)):
        for j in words[i]:
            if(j in possible):
                result[i] = True
            else:
                result[i] = False
                break
    
    return result

print(possibleWords([1,2,3], ["abc", "abcdef", "aaaa", "ghi", "adbecf"]))

