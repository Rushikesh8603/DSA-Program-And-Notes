# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:



        def give(node):
            final = [0]
            def inorder(node):
                if node is None:
                    return 0
                        
                left = inorder(node.left) 

                right = inorder(node.right)
                final[0] = max(final[0] , left + right + 1)
                ans = max(left , right) + 1 
                return ans 

            inorder(node)

            return final[0]
        return give(root)-1

        