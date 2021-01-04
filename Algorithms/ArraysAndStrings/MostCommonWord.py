def mostCommonWord(paragraph, banned):
    """
    Given a paragraph and a list of banned words, the 
    algorithm returns the most common word in that paragraph.

    Time: O(n+m)
    Space: O(n+m)
    """
    #clean the string (get rid of punctuations, make all lower case)
    clean = ''.join([i.lower() if i.isalnum() else ' ' for i in paragraph])
    clean = clean.split(" ")
    #place the banned words in a hash table for O(1) lookup
    banned_hash = {}
    for i in banned:
        banned_hash[i] = True
    
    words = {}
    maxi = -1
    word = ""
    #go through the cleaned words and record its frequencies
    for i in clean:
        if(i not in banned_hash and i!=''):
            if(i not in words):
                words[i]=1
                if(words[i] > maxi):
                    maxi = words[i]
                    word = i
            else:
                words[i]+=1
                if(words[i] > maxi):
                    maxi = words[i]
                    word = i
    return word

paragraph = "Bob. hIt, baLl,and BALL flew"
banned = ["bob", "hit"]
assert "ball" == mostCommonWord(paragraph, banned)