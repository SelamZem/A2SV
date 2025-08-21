class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Given an integer array nums
        # not contain duplicated triplet
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            target = -nums[i]
            ptr1, ptr2 = i + 1, n - 1
            while ptr1 < ptr2:
                total = nums[ptr1] + nums[ptr2]
                if total == target:
                    res.append([nums[i], nums[ptr1], nums[ptr2]])
                    ptr1 += 1
                    ptr2 -= 1
                    while ptr1 < ptr2 and nums[ptr1] == nums[ptr1-1]:
                        ptr1 += 1
                    while ptr1 < ptr2 and nums[ptr2] == nums[ptr2+1]:
                        ptr2 -= 1
                elif total < target:
                    ptr1 += 1
                else:
                    ptr2 -= 1

        return res
