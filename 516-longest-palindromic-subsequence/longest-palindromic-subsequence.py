# Neetcode
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        length = 0
        memo = [[-1 for i in range(n)] for j in range(n)]
        

        def dp(i,j):
            nonlocal length
            if i>j:
                return 0
            if i==j:
                return 1
            if memo[i][j]!=-1 :
                return memo[i][j]

            if s[i] == s[j]:
                if i==j:
                    length=1
                else:
                    length=2
                memo[i][j]= length + dp(i+1, j-1)
            else:
                memo[i][j] = max(dp(i+1,j), dp(i, j-1))

            return memo[i][j]

        return dp(0, n-1)