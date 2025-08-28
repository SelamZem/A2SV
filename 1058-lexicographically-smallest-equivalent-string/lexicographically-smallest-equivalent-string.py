class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
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

        i = 0
        while i < n:
            c, d = s1[i], s2[i]
            union(c, d)
            i += 1

        res = []
        for x in baseStr:
            a = ord(x) - ord('a')
            ch = find(a)
            res.append(chr(ch + ord('a')))

        return ''.join(res)
