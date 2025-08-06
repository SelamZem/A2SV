class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # annual photo
        # non decreasing order by height
        ans = 0
        # the simpler soln
        
        hei = heights.copy()
        hei.sort()
        for i in range(len(heights)):
            if hei[i]!=heights[i]:
                ans+=1

        return ans