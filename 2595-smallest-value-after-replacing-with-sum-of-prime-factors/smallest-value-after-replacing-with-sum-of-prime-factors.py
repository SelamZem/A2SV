class Solution:
    def smallestValue(self, n: int) -> int:
        
        def prime(x):
            res =0
            d=2
            while x>1:
                while x%d==0:
                    x//=d
                    res+=d
                d+=1
            return res

        while n!=prime(n):
            n = prime(n)
        return n





    

        