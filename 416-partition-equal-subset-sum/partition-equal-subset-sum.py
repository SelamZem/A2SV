class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # return true if you can partition the array into two subsets be equal
        # subset set is total//2

        total = sum(nums)

        if total%2!=0:
            return False

        target = total//2

        # check if there any subset that gives target(half_total)

        n = len(nums)
        memo = {}
       

        def dp(i, half_sum):

            if half_sum==target:
                return True
            if half_sum > target or i >= n:
                return False
    
            if (i,half_sum) in memo:
                return memo[(i,half_sum)]

            # include = dp(i+1,half_sum+nums[i])
            # exclude = dp(i+1,half_sum)
            # memo[(i,half_sum)] = include or exclude
            memo[(i, half_sum)] = (
                dp(i + 1, half_sum + nums[i]) or
                dp(i + 1, half_sum)
            )



            return memo[(i,half_sum)]
            
        return dp(0,0)