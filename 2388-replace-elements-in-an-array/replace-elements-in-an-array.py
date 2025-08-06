class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # 0 indexed array
        # n distinct positive integers
        # apply m operations
        # replace operation[i][0] with operation[i][1]

        
        # for x, y in operations:
        #     i=nums.index(x)
        #     nums[i] = y

        # return nums

        indx = defaultdict(int)
        valuex = defaultdict(int)

        for i, x in enumerate(nums):
            indx[i] = x
            valuex[x]=i

        for x,y in operations:
            a = valuex[x]
            indx[a] = y
            del valuex[x]
            valuex[y] = a
            

        res =[]
        for x in indx:
            res.append(indx[x])

        return res
