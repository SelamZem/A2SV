class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        # topological sort

        # terminal is when there is no outgoing edges...
        # safe nodes are nodes that, the edges only directed to the terminal or other safe nodes

        # create graph again, but keep track of the outgoing than the incomings...so it will be reversed

        n = len(graph)
        my_graph = defaultdict(list)
        outgoing = [0] * n
        res = []

        for i,x in enumerate(graph):
            y = len(x)
            for j in range(y):
                my_graph[x[j]].append(i)
                outgoing[i]+=1

                
        queue = deque()
        for i in range(n):
            if outgoing[i]==0:
                queue.append(i)
                res.append(i)

        while queue:
            a = queue.popleft()
            for x in my_graph[a]:
                outgoing[x] -=1
                if outgoing[x]==0:
                    queue.append(x)
                    res.append(x)


        return sorted(res)

        