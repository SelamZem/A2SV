class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # given 0 indexed array ... consists of non negative integers
        # apply n-1 operations

        n = len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                x = nums[i]*2
                nums[i]=x
                nums[i+1] = 0
                i+=1

        ptr1, ptr2 = 0, 0
        while ptr2<n:
            if nums[ptr1] and nums[ptr2]:
                ptr1+=1
            else:
                if nums[ptr1] == 0 and nums[ptr2]!=0:
                    nums[ptr1]=nums[ptr2]
                    nums[ptr2]=0
                    ptr1+=1

            ptr2+=1

        return nums
