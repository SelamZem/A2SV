class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n= len(obstacleGrid[0])
        memo ={}
        direction =[[0,1],[1,0]]
        ans = 0
        def dp(row, col):
            

            if row<0 or row>m-1 or col<0 or col>n-1:
                return 0 
            if obstacleGrid[row][col]==1:
                return 0
            if row==m-1 and col==n-1:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            res =0
            for x,y  in direction:
                newr, newc = row+x, col+y
                res+= dp(newr, newc)                

            memo[(row, col)] =res
            return res
            
        ans=dp(0,0)
        return ans
    
        