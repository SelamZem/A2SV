class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        graph = {i: i for i in range(26)}

        def find(x):
            if graph[x] != x:
                graph[x] = find(graph[x])
            return graph[x]

        def union(x, y):
            ox = ord(x) - ord('a')
            oy = ord(y) - ord('a')
            rootx = find(ox)
            rooty = find(oy)
            if rootx == rooty:
                return
            if rootx < rooty:
                graph[rooty] = rootx
            else:
                graph[rootx] = rooty

        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[3])

        for eq in equations:
            if eq[1:3] == "!=":
                ox = ord(eq[0]) - ord('a')
                oy = ord(eq[3]) - ord('a')
                if find(ox) == find(oy):
                    return False

        return True
