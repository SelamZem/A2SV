from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_pro = [1] * n
        suff_pro = [1] * n
        res = [1] * n

        pro = 1
        for i in range(n):
            pre_pro[i] = pro
            pro *= nums[i]

        pro = 1
        for i in range(n-1, -1, -1):
            suff_pro[i] = pro
            pro *= nums[i]

        for i in range(n):
            res[i] = pre_pro[i] * suff_pro[i]

        return res
