# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.current = TreeNode(-1)
        self.dummy = self.current
        def traverse_BST(root):
            if root is None:
                return 
            traverse_BST(root.left)
            node = TreeNode(root.val)
            self.dummy.right = node 
            self.dummy = node
            traverse_BST(root.right)
            return 
        traverse_BST(root)
        return self.current.right
    
    


        