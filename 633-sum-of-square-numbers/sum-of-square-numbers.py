class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        # are a and b successive?
        # mid = c//2 + 1
        # m_squared = []

        # for i in range(mid+1):
        #     m_squared.append(i**2)

        # print(m_squared)

        # for i in range(len(m_squared)):
        #     target =  c-m_squared[i]
        #     if target in m_squared:
        #         return True
        # return False

        mid = int(c**0.5)
        ptr1, ptr2 = 0, mid
        while ptr1<=ptr2:
            target = ptr1*ptr1 + ptr2*ptr2
            if target==c:
                return True
            elif target>c:
                ptr2-=1
            else:
                ptr1+=1

        return False

        