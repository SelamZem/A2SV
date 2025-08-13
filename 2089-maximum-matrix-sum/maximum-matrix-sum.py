class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # given nxn matrix
        # operation
            # two adjancent elements and multiply each by -1

        n = len(matrix)
        total = 0
        count = 0
        min_val = float('inf')
        for i in range(n):
            for j in range(n):
                a = matrix[i][j]
                total += abs(a)
                min_val = min(min_val, abs(a))
                if a<0:
                    count+=1

        print(total)
        print(min_val)
        if count%2==0:
            return total
        return total-2*min_val



