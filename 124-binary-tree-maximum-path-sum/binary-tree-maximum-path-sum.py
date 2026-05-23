# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')

        def path_traverse(root):
            if root == None:
                return 0 
            left = path_traverse(root.left)
            right = path_traverse(root.right)
            self.max_path_sum = max(self.max_path_sum , left + right + root.val)
            return max(0 , root.val + max(left ,right))
        path_traverse(root)

        return self.max_path_sum

















        