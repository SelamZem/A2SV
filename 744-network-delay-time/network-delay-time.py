class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # neetcode
        graph = defaultdict(list)
        for x, y, z in times:
            graph[x].append((y, z))

        min_heap = [(0, k)]
        visited = set()
        t = 0

        while min_heap:
            w, v = heapq.heappop(min_heap)
            if v in visited:
                continue
            visited.add(v)
            t = max(t, w)

            for m, a in graph[v]:
                if m not in visited:
                    heapq.heappush(min_heap, (w + a, m))

        return t if len(visited) == n else -1
