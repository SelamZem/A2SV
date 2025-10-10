class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        effort_matrix = [[float('inf')] * cols for _ in range(rows)]
        effort_matrix[0][0] = 0
        min_heap = [(0, (0, 0))]

        while min_heap:
            current_effort, (r, c) = heappop(min_heap)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    next_effort = max(abs(heights[nr][nc] - heights[r][c]), effort_matrix[r][c])
                    if next_effort < effort_matrix[nr][nc]:
                        effort_matrix[nr][nc] = next_effort
                        heappush(min_heap, (next_effort, (nr, nc)))
        
        return effort_matrix[rows - 1][cols - 1]
