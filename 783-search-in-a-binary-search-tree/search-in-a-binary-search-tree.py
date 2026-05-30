# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return None

        if root.val == val:
            return root
        if root.val > val :
            left = self.searchBST(root.left , val)
            if left is not None:
                return left 
        else:
            right = self.searchBST(root.right, val)
            if right is not None:
                return right
        
        return 


    


