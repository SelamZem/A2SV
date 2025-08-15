class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # for the second example ....
        # if we chose 1(out of 3 for the first one) we left with 2 numbers(2 and 3)...if we chose 2 we will be left with 3 or if we chose 3 2 will be the last choice for this one

        # start at the index 0


        # neetcode(youtube)
       
        n = len(nums)
        res = []
        my_dict = Counter(nums)

        def backtrack(curr):
            if len(curr)==n:
                res.append(curr.copy())
                return 

            for x in my_dict:
                if my_dict[x]>0:
                    my_dict[x]-=1
                    curr.append(x)
                    backtrack(curr)

                    my_dict[x] +=1
                    curr.pop()

        
        backtrack([])
        return res
            
            
            