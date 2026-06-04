# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        arr = []

        def Traverse(root):

            if root is None:
                return
            Traverse(root.right)
            arr.append(root.val)
            if len(arr) >= 2:
                self.ans = min(self.ans , abs(arr[-1]- arr[-2]))
            Traverse(root.left)
            return 

        Traverse(root)
        return self.ans
    
    
    
    
    
        

            
            
            



            

    

        