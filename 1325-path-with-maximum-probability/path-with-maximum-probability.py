class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # create the graph
        graph = defaultdict(list)
        for i in range(len(edges)):
            origin, dest = edges[i]
            graph[origin].append([dest, succProb[i]])
            graph[dest].append([origin, succProb[i]])

        max_heap = [(-1, start_node)]
        visited = set()

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            visited.add(node)

            if node==end_node:
                return prob * -1
            
            for nei, neiprob in graph[node]:
                if nei not in visited:
                    heapq.heappush(max_heap, (prob*neiprob, nei))
        return 0

        