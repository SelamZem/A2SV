class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # find nums that added to zero
        # all length n

        my_dict = defaultdict(int)

        for x in nums1:
            for y in nums2:
                my_dict[x+y]+=1

        count = 0

        for a in nums3:
            for b in nums4:
                if -(a+b) in my_dict:
                    count += my_dict[-(a+b)]

        return count



