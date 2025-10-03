class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # There are n cities numbered from 0 to n-1
        graph = defaultdict(list)
        for x, y,z in edges:
            graph[x].append([y, z])
            graph[y].append([x, z])
        
        def dijkstra(src):
            min_heap = [(0,src)]
            visited = set()

            while min_heap:
                dist, node = heapq.heappop(min_heap)
                if node in visited:
                    continue
                visited.add(node)
                for nei, dest in graph[node]:
                    distth = dest + dist
                    if distth<=distanceThreshold:
                        heapq.heappush(min_heap, (distth, nei))

            return len(visited) - 1
            
        res, min_count = -1, float('inf')
        for i in range(n):
            count = dijkstra(i)
            if count<=min_count:
                res, min_count = i, count
        return res