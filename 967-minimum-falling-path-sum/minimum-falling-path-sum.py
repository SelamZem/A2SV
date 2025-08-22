class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Given nxn matricx 
        ## return the minimum sum of any falling path through matrix

        n = len(matrix)
        memo = {}
        def dfs(r, c):
            if r >=n:
                # to the lowest row
                return 0
            if c<0 or c>=n:
                return float("inf")
            if (r,c) in memo:
                return memo[(r,c)]
            # (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
            res = min(dfs(r+1, c+1), dfs(r+1, c), dfs(r+1, c-1))
            memo[(r,c)] = res + matrix[r][c]

            return memo[(r,c)]

        ans = float("inf")
        for c in range(n):
            ans = min(ans, dfs(0, c))

        return ans
            
