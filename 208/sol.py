# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class Node():
    def __init__(self):
        self.end = False
        self.keys = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['__end__'] = True 

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            if char not in curr:
                return False 
            curr = curr[char]

        return True if '__end__' in curr else False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False 
            char = curr[char]
        
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  
print(trie.search("app"))
print(trie.startsWith("app"))
#trie.insert("app")
#print(trie.search("app"))