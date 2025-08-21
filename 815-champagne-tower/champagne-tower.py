class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # utube
        # first build the pyramid
        pyramid = [[0.0] * k for k in range(1,query_row+2)]
        pyramid[0][0] = poured


        for i in range(query_row):
            for j in range(i+1):
                overflow = (pyramid[i][j]-1.0)/2.0
                if overflow>0:
                    pyramid[i+1][j]+=overflow
                    pyramid[i+1][j+1] +=overflow

        return min(1.0, pyramid[query_row][query_glass])