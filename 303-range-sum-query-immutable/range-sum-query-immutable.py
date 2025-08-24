from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums 

    def sumRange(self, left: int, right: int) -> int:
        rangeSum = 0
        while left <= right:
            rangeSum += self.arr[left]
            left += 1
        return rangeSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)