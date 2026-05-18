# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_height(node):
            if node is None:
                return 0
                
            # 1. Check Left (and short-circuit if unbalanced)
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
                
            # 2. Check Right (and short-circuit if unbalanced)
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
                
            # 3. Check current node's balance
            if abs(left_height - right_height) > 1:
                return -1
                
            # 4. If balanced, return actual height
            return max(left_height, right_height) + 1
            
        # If the root returns -1, the tree is unbalanced. 
        # Any other number means it is balanced.
        return check_height(root) != -1

        



        