class Trie:
    '''
    The following is a Trie implementation using HashMaps

    Time for standard operations: O(n)
    Space: O(n)
    '''

    def __init__(self):
        self.children = [{}, False]

    def insert(self, word: str) -> None:
        i, curr_node = 0, self.children

        while i < len(word) and word[i] in curr_node[0]:
            curr_node = curr_node[0][word[i]]
            i += 1
        
        while i < len(word):
            curr_node[0][word[i]] = [{}, False]
            curr_node = curr_node[0][word[i]]
            i += 1
        
        curr_node[1] = True

    def search(self, word: str) -> bool:
        i, curr_node = 0, self.children

        while i < len(word) and word[i] in curr_node[0]:
            curr_node = curr_node[0][word[i]]
            i += 1

        return i == len(word) and curr_node[1]

    def startsWith(self, prefix: str) -> bool:
        i, curr_node = 0, self.children 

        while i < len(prefix) and prefix[i] in curr_node[0]:
            curr_node = curr_node[0][prefix[i]]
            i += 1

        return i == len(prefix)

trie = Trie()
trie.insert("apple")
assert trie.search("apple") ==  True
assert trie.search("app") == False
assert trie.startsWith("app") == True
trie.insert("app")
assert trie.search("app") == True