def ladderLength(beginWord, endWord, wordList):
    """
    Given a begin word, end word, and a word list, the
    algorithm finds the minimum number of transformation 
    required using the words in the word list to get the 
    end word. Each word can only be changed by one character.
    Let m,n be the length of the words, word list, respectively

    Time: (nm^2)
    Space: O(nm^2)
    """
    words = {}
    #store all the words in a dictionary for keeping track of visited 
    for i in wordList:
        words[i] = True
    #end word must be present in the word list for the transformation
    if(endWord not in words):
        return 0
    #queue bfs
    neighbours = [beginWord]
    edit = 0
    #all the letters in the alphabet that are required to form the combinations
    alph = "abcdefghijklmnopqrstuvwxyz"
    #perform bfs
    while neighbours:
        #go through the current level
        for i in range(len(neighbours)):
            #pop 'neighbours' from the queue in the current level
            beginWord = neighbours.pop(0) 
            #go through the current word and find all possible combinations
            for k in range(len(beginWord)):
                for j in alph:
                    temp = beginWord[:k]+j+beginWord[k+1:]
                    #check if the new possible word is in the word list and not visited before
                    if(temp in words and words[temp]):
                        #if its the end word, we are done and return current depth + 2 (we add 1 for curr level and 1 for next level)
                        if temp == endWord:
                            return edit+2
                        #add it to queue
                        neighbours.append(temp)
                        #set as visited
                        words[temp] = False
        edit+=1
    #if beginWord == endWord, it is possible
    return edit if beginWord == endWord else 0