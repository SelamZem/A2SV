class Solution:
    def numberOfPairs(self, nums: List[int]) -> List:

        my_dict = defaultdict(int)
        res = [0, 0]

        for x in nums:
            my_dict[x]+=1

        for x in my_dict:
            left = my_dict[x]%2
            paired = my_dict[x]//2
            res[0] +=paired
            res[1] +=left

        return res
