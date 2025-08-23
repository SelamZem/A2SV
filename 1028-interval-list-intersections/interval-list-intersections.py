class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Given two lists of closed intervals
        # sorted order
        res = []

        # equal len??

        if not firstList or not secondList:
            return res

        # things i should handle
        # if i have more than two intervals that fit into  1 interval of the other list
        m = len(secondList)
        n = len(firstList)
        ptr1, ptr2 = 0, 0

        # if one of them reach the end break the loop
        while ptr1<n and ptr2<m:
            a,b = firstList[ptr1]
            x,y = secondList[ptr2]

            start = max(a, x)
            end = min(b,y)
            
            if start<=end:
                res.append([start, end])

            if b<y:
                ptr1+=1
            else:
                ptr2+=1

        return res
