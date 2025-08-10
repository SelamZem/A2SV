class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        memo = {}
        def dfs(i, j):
            if j == 0 or j == i:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = dfs(i - 1, j - 1) + dfs(i - 1, j)
            return memo[(i, j)]

        result = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                row.append(dfs(i, j))
            result.append(row)
            
        return result



                
