class Solution:
    def jump(self, nums: List[int]) -> int:
        # it is kinda similar to the coins problem??

        n = len(nums)
        # what should i return at index zero??
        memo = {}

        def dp(i):
            if i>=n-1:
                return 0

            if i in memo:
                return memo[i]

            min_jump=float('inf')
            
            # the max they can jump from  to other is nums[i]
            jump_upto = nums[i]

            for j in range(1, jump_upto+1):
                nxt = i + j
                if nxt<n:
                    jump = 1+dp(nxt)
                    min_jump = min(min_jump, jump)

            memo[i] = min_jump
            return memo[i]

        return dp(0)