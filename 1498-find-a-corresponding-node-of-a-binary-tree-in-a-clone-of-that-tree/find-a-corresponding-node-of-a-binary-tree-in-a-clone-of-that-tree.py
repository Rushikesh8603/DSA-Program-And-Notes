# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def TraverseTree(node):
            if node is None:
                return None

            if node.val == target.val:
                return node 
            
            left = TraverseTree(node.left)
            if left is not None:
                return left
            right = TraverseTree(node.right)
            if right is not None:
                return right

            return left or right 
        
        return TraverseTree(cloned)
    
        
        




        
    
        