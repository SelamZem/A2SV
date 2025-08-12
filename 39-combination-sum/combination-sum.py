class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #neetcode
        result = []

        # i as pointer, curr(to track current sum),  total

        def backtrack(i,curr, total):
            # if total is equal to target...add current to result
            if total==target:
                result.append(curr.copy())
                return 
            if i>=len(candidates) or total>target:
                return

            # first add the number and check for every combination befor going to the next one
            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            curr.pop()
            backtrack(i+1, curr, total)

        backtrack(0,[],0)

        return result