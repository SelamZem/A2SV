class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        memo = {}
        result = []

        def dp(i,j):
            if j==0 or j==i:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]

            memo[(i,j)] = dp(i-1,j-1) + dp(i-1, j)

            return memo[(i,j)]

        for j in range(rowIndex+1):
            x = dp(rowIndex,j)
            result.append(x)

        return result

    