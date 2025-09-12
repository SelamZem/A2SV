class Solution:
    def isThree(self, n: int) -> bool:

        factor = 0

        for i in range(2, n-1):
            if n%i==0:
                factor+=1
            if factor>1:
                return False

        if factor==0:
            return False
        return True
        