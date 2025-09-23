class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            curr = ord(ch) - ord('a')
            if node.children[curr] is None:
                node.children[curr] = TrieNode()
            node = node.children[curr]
        node.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            order = ord(ch) - ord('a')
            if curr.children[order] is None:
                return False
            curr = curr.children[order]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            order = ord(ch) - ord('a')
            if curr.children[order] is None:
                return False
            curr = curr.children[order]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)