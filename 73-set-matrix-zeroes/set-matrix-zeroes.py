class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first check if 0 is in the  row...then column

        n = len(matrix) # row
        m = len(matrix[0]) # column

        array1 = []
        array2 = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    array1.append(i)
                    array2.append(j)

        for i in array1:
            for j in range(m):
                matrix[i][j]=0

        for j in array2:
            for i in range(n):
                matrix[i][j]=0


        return matrix






