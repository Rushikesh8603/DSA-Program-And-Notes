# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
            if root is None:
                return root
            if root.val == 2 and (root.left.val == 1 or root.right.val == 1 ):
                return True

            if root.val == 3 and (root.left.val== 0 or root.right.val == 0 ):
                return False

            right = self.evaluateTree(root.right)
            left = self.evaluateTree(root.left)

            if root.val == 3:
                return bool(left) and bool(right) 
            if root.val == 2:
                return bool(left) or bool(right) 
            
            return bool(root.val) 

    #tc = 0(N) N is the number of nodes of the given tree
    #sc = 0(H) H is hte height of the given tree 
    

            



        