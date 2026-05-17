# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True

        def height(root):
            if root == None:
                return 0 
            left = height(root.left)
            right = height(root.right)
            if max(left , right ) - min(left , right ) > 1:
                self.flag = False
            return max(left , right) + 1 
        height(root)
        return self.flag
    





        