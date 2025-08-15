class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # given 2d integer array ranges

        number_set = set()
        for x,y in ranges:
            for i in range(x, y+1):
                number_set.add(i)

        for j in range(left, right+1):
            if j not in number_set:
                return False

        return True