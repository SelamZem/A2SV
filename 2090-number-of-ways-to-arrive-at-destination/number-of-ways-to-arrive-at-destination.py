class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for x, y, z in roads:
            graph[x].append([y, z])
            graph[y].append([x, z])
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        min_heap = [(0, 0)]
        
        while min_heap:
            cur_dist, node = heapq.heappop(min_heap)
            if cur_dist > dist[node]:
                continue
            for nei, time in graph[node]:
                new_dist = cur_dist + time
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    ways[nei] = ways[node]
                    heapq.heappush(min_heap, (new_dist, nei))
                elif new_dist == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[n - 1] % MOD
