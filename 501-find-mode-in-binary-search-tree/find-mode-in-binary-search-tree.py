# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        my_dict = defaultdict(int)
        def find_mode(node):
            if not node:
                return
            my_dict[node.val] +=1
            find_mode(node.left)
            find_mode(node.right)
        
        find_mode(root)

        if not my_dict:
            return res

        max_freq = max(my_dict.values())
        for x in my_dict.keys():
            if my_dict[x] == max_freq:
                res.append(x)
        
        return res



        