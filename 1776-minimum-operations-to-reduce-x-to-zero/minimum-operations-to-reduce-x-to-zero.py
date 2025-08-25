class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
    
        # memo ={}
        # def dp(left, right, target):
        #     if target==x:
        #         return 0
        #     if left>right or target>x:
        #         return float('inf')

        #     if (left, right, target) in memo:
        #         return memo[(left, right, target)]

        #     take = 1 + dp(left+1, right, target+nums[left])
        #     skip = 1 + dp(left, right-1, target+nums[right])

        #     memo[(left, right, target)] = min(take, skip)

        #     return memo[(left, right, target)]

        # res = dp(0, len(nums)-1, 0)
        # return -1 if res==float("inf") else res


        n = len(nums)
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1
        if target == 0:
            return n

        min_len = float('inf')
        window = []
        window_sum = 0

        for right in range(n):
            window_sum += nums[right]
            window.append(nums[right])

            while window_sum > target and window:
                window_sum -= window[0]
                window = window[1:]

            if window_sum == target:
                y = n - len(window)
                min_len = min(min_len, y)

        return -1 if min_len == float('inf') else min_len