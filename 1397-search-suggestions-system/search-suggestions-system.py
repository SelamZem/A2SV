class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            if len(node.suggestions) < 3:
                node.suggestions.append(word)
                node.suggestions.sort()
            elif word < node.suggestions[-1]:
                node.suggestions[-1] = word
                node.suggestions.sort()
    
    def get_suggestions(self, prefix):
        node = self.root
        result = []
        for char in prefix:
            if char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                result.extend([[] for _ in range(len(prefix) - len(result))])
                break
        return result

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        return trie.get_suggestions(searchWord)
