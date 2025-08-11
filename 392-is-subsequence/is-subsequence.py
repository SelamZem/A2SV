class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # check if s is subsequence of t

        # if len(s)>len(t) return false

        # idk how this is dynamic/2 ptr is easier
        m = len(s)
        n = len(t)
        memo = {}

        if m>n:
            return False

        def dp(i, j):
            if i==m:
                return True
            if j==n:
                return False
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i]==t[j]:
                memo[(i,j)]=dp(i+1, j+1)
            else:
                memo[(i,j)]=dp(i, j+1)
            return memo[(i,j)]

        return dp(0,0)

            