def suggest(searchWord, possibleWords):
    """
    Given a list of possible suggestion words and a search query, the 
    algorithm finds suggested words (max 3 words) based on the sequence
    of each character typed from the searchWord.

    Time: O(nlogn) 
    Space: O(n)
    """
    #sorting to perform binary search
    possibleWords.sort()
    word = ""
    suggested = []
    result = []
    for i in range(len(searchWord)):
        #forming the sequence of each character typed from the searchWord
        word+=searchWord[i]
        #performing binary search to find the possible suggested words (since sorted lexicographically)
        index = binarySearch(possibleWords, word)
        for j in range(index, min(len(possibleWords), index + 3)):
            #matching prefix will determine possible suggestion word
            if(word == possibleWords[j][:i+1]):
                suggested.append(possibleWords[j])
            j+=1
        result.append(suggested)
        suggested = []
    return result

#binary search to find out what index to insert to maintain sorted property
def binarySearch(A, target):
    low = 0
    high = len(A)
    mid = (low + high) //2
    while low < high:
        if A[mid] < target: 
            low = mid + 1
        else: 
            high = mid
        mid = (low + high)//2
    return low

A = ["mobile","mouse","moneypot","monitor","mousepad"]
print(suggest("mouse", A))
