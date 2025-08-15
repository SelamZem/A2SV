class Solution:
    def isHappy(self, n: int) -> bool:
        # if the number repeats itself not happy

        repeat = set()
        while n!=1 and n not in repeat:
            squared_sum = 0
            repeat.add(n)
            while n>0:
                rem = n%10
                n = n//10
                squared_sum += (rem**2)

            n = squared_sum

        return n==1

