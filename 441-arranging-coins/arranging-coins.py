class Solution:
    def arrangeCoins(self, n: int) -> int:
        # bruteforce
        res = 0

        i = 1
        while n>0:
            n = n-i
            if n<0:
                break
            else:
                res+=1
            i+=1
        return res