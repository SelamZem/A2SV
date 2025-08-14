class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # already ordered matrix
        n = len(matrix)
        heap = []
       
        for r in range(min(n, k)): 
            heapq.heappush(heap, (matrix[r][0], r, 0))

        count = 0
        while heap:
            val, r, c = heapq.heappop(heap)
            count += 1
            if count == k:
                return val
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
