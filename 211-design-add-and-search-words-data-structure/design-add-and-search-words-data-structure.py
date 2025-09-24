class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            curr = ord(ch) - ord('a')
            if not node.children[curr]:
                node.children[curr] = Trie()
            node = node.children[curr]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if not node:
                return False
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == '.':
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            curr = ord(ch) - ord('a')
            return dfs(node.children[curr], i + 1)

        return dfs(self.root, 0)
