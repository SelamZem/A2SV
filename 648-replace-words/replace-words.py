class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
    
        root = Trie()
        for word in dictionary:
            node = root
            for ch in word:
                curr = ord(ch) - ord('a')
                if not node.children[curr]:
                    node.children[curr] = Trie()
                node = node.children[curr]
            node.is_end = True

        sent = sentence.split()
        to_be_returned = []

        for word in sent:
            node = root
            the_word = ""
            for ch in word:
                curr = ord(ch) - ord('a')
                if not node.children[curr]:
                    the_word = word 
                    break
                node = node.children[curr]
                the_word += ch
                if node.is_end:
                    break 
            to_be_returned.append(the_word) 

        return " ".join(to_be_returned)
