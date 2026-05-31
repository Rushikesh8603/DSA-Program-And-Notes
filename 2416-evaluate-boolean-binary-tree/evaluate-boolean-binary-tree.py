# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def evaluate(root):
            if root is None:
                return root

            right = evaluate(root.right)
            left = evaluate(root.left)


            if root.val == 3:
                return left and right 
            if root.val == 2:
                return left or right 
            
            return root.val 

        ans = evaluate(root)
        if ans == 1 :
            return True
        else:
            return False
        


            



        