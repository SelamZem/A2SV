class Solution:
    def countBits(self, n: int) -> List[int]:
        # given an integer n
        # return array(len(n+1))

        ans = [0] * (n+1)
        ans[0] = 0

        for i in range(1,n+1):
            ans[i] = i%2 + ans[i//2] 

        return ans