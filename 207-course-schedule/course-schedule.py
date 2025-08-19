class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        graph = defaultdict(list)
        incomings = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            incomings[u] +=1

        queue = deque()
        for i,x in enumerate(incomings):
            if x==0:
                queue.append(i)

        while queue:
            q = queue.popleft()
            for y in graph[q]:
                incomings[y]-=1
                if incomings[y]==0:
                    queue.append(y)

        if sum(incomings)==0:
            return True
        return False