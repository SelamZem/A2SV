# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = 0
        def backtrack(node, curr):
            nonlocal res
            if not node:
                return

            curr = curr*10 + node.val

            if not node.left and not node.right:
                res +=curr
                print(res)
                return
            
            

            backtrack(node.left, curr)
            backtrack(node.right, curr)

        backtrack(root, 0)
        return res
        