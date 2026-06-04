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
        self.temp = float('inf')

        def Traverse(root):
            if root is None:
                return
            Traverse(root.right)
            self.ans = min(self.ans ,abs(root.val - self.temp))
            self.temp = root.val
        
            Traverse(root.left)
            return 

        Traverse(root)
        return self.ans
    
    #tc = sc = 0(N) n is hte number of node in the tree 
    
    
    
    
    
        

            
            
            



            

    

        