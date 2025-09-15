class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # factors = []

        # a = n//2+1
        # x=n
        # for i in range(1,a):
        #     if n%i==0:
        #         factors.append(i)

        # factors.append(x)
        # print(factors)
        # return factors[k-1] if len(factors)>=k else -1

        b = 0
        for i in range(1,n+1):
            if n%i==0:
                b+=1
            if b==k:
                return i
        return -1