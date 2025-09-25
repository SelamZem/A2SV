class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.val = 0 


class MapSum:
    def __init__(self):
        self.root = Trie()
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        
        node = self.root
        for ch in key:
            curr = ord(ch) - ord('a')
            if not node.children[curr]:
                node.children[curr] = Trie()
            node = node.children[curr]
            node.val += diff 

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            curr = ord(ch) - ord('a')
            if not node.children[curr]:
                return 0
            node = node.children[curr]
        return node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)