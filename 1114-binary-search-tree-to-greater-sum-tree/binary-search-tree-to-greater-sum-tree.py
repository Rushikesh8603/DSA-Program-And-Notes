# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.running_sum = 0 
        def traverse(root):

            if root == None:
                return 

            right = traverse(root.right)

            self.running_sum+= root.val

            root.val = self.running_sum

            left = traverse(root.left )
            
            return

        traverse(root)

        return root 
    



        






        







