class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        dist = [[float('inf')] * n for _ in range(m)]
        
        dq = deque([(0, 0)])
        dist[0][0] = grid[0][0]
        
        while dq:
            r, c = dq.popleft()
            
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = dist[r][c] + grid[nr][nc]
                    if new_cost < dist[nr][nc] and new_cost < health:
                        dist[nr][nc] = new_cost
  
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))

                        else:
                            dq.append((nr, nc))
        
        return dist[m-1][n-1] < health
