class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        memo =[-1]*n

        def dfs(i):

            if i>=n:
                return 0
            
            if memo[i]!=-1:
                return memo[i]
        
            points, brainpower = questions[i]
            include = points + dfs(i+brainpower+1) 
            exclude =  dfs(i+1)
        
            memo[i] =  max(include, exclude)
            return memo[i]



        return dfs(0)          