class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        x, y = 0, n-1
        

        def find_t(l, r, target):
            if l > r:  
                return -1
            mid = (l+r)//2

            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                return find_t(mid+1, r, target)
            else:
                return find_t(l, mid-1, target)
       

        return find_t(x,y, target)