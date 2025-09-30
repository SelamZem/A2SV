class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # root = Trie()

        # for word in wordDict:
        #     node = root
        #     for ch in word:
        #         curr = ord(ch)- ord(a)
        #         if not node.children[curr]:
        #             node.children[curr] = Trie()
        #         node = node.children[curr]
        #     node.is_end=True


        ## neetcode solution with DP
        dp = [False] * (len(s) + 1)
        dp[len(s)] =True

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # base case

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    if dp[i + len(w)]:
                        dp[i] = True
                        break

        return dp[0]
