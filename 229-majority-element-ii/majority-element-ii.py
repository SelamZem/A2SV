class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # given : size n
        # elements that appeared more n/3
        
        n = len(nums)
        my_dict = Counter(nums)
        a = n//3
        ans = []
        for x in my_dict:
            if my_dict[x]>a:
                ans.append(x)

        return ans

