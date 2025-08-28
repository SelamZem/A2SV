class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        res = []

        n = len(edges)
        my_dict = {i: i for i in range(1, n+1)}

        def find(x):
            if my_dict[x] != x:
                my_dict[x] = find(my_dict[x]) 
            return my_dict[x]

        def union(x, y):
            nonlocal res  
            rootx = find(x)
            rooty = find(y)

            if rootx != rooty:
                my_dict[rootx] = rooty
            else:
                res = [x, y]

        for x, y in edges:
            union(x, y)

        return res
