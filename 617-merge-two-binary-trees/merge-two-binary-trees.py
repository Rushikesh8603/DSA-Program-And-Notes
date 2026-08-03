# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         #base condition 

#         if root1 is None or root2 is None:
#             return root1 or root2
        
#         root2.val+= root1.val
#         print(root2.val)

#         if root1.left is not None and root2.left is None:
#             Node = TreeNode(0)

#             root2.left = Node
#             print('printing', root2.left)

#         self.mergeTrees(root1.left , root2.left)

#         if root1.right is not None and root2.right is None:
#             Node = TreeNode(0)
    
#             root2.right = Node

#         self.mergeTrees(root1.right, root2.right)

#         return root2


        

        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. BASE CASES: If one node is missing, return the other immediately.
        # This attaches entire existing subtrees in O(1) time without traversing them!
        if not root1:
            return root2
        if not root2:
            return root1
        
        # 2. MERGE VALUES: Since both exist, add them together in-place
        root1.val += root2.val
        
        # 3. REWIRE POINTERS: Catch the returned nodes and update branches
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        # 4. RETURN THE MODIFIED MASTER NODE
        return root1

        






        