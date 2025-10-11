class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Trie()
                node = node.children[ch]
            node.is_end = True

        result = ""
        for word in words:
            node = root
            valid = True
            for ch in word:
                node = node.children[ch]
                if not node.is_end:
                    valid = False
                    break
            if valid:
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
        return result
