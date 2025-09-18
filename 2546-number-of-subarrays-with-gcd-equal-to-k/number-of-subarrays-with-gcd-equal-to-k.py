class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def gcd(a, b):
            if b == 0:
                return a  
            return gcd(b, a % b)

        res = 0

        for x in nums:
            if x == k:
                res += 1

        i = 0
        while i < n:
            g = nums[i]
            j = i + 1
            while j < n:
                g = gcd(g, nums[j])
                if g == k:
                    res += 1
                elif g < k:
                    break
                j += 1
            i += 1

        return res
