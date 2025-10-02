class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        incomings = [0] * numCourses
        for ind, dep in prerequisites:
            if ind not in graph:
                graph[ind] = []
            graph[ind].append(dep)
            incomings[dep] += 1
        queue = []
        for i, x in enumerate(incomings):
            if x == 0:
                queue.append(i)
        prereq = [set() for _ in range(numCourses)]
        while queue:
            node = queue.pop(0)
            if node in graph:
                for nei in graph[node]:
                    prereq[nei] |= prereq[node] | {node}
                    incomings[nei] -= 1
                    if incomings[nei] == 0:
                        queue.append(nei)
        result = []
        for u, v in queries:
            result.append(u in prereq[v])
        return result
