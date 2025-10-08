class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # given 0-indexed strings(source and target)
        # both are length of n
        #2 arrays (orginal and changed)
        # cost(where cost[i] represents the cost of changing the char for orginal[i] to

        #neetcode
        # Build adjacency list
        adj = defaultdict(list)
        for src, dst, cur_cost in zip(original, changed, cost):
            adj[src].append((dst, cur_cost))
        
        # Dijkstra
        def dijkstra(start):
            heap = [(0, start)]
            dist = {chr(i + ord('a')): math.inf for i in range(26)}
            dist[start] = 0
            
            while heap:
                curr_cost, node = heapq.heappop(heap)
                if curr_cost > dist[node]:
                    continue
                for nei, edge_cost in adj[node]:
                    if curr_cost + edge_cost < dist[nei]:
                        dist[nei] = curr_cost + edge_cost
                        heapq.heappush(heap, (dist[nei], nei))
            return dist
        
        min_cost_maps = {c: dijkstra(c) for c in set(source)}
        

        total = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            cost_to_t = min_cost_maps[s].get(t, float('inf'))
            if cost_to_t == float('inf'):
                return -1
            total += cost_to_t
        
        return total

        