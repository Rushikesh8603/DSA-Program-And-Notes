# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.contaner = []
        def traverse(root):
            if root == None:
                self.contaner.append('none')
                return 

            self.contaner.append(root.val)
            
            left = traverse(root.left)
            right = traverse(root.right)
        traverse(p)
        print("arr1", self.contaner)
        arr1 = self.contaner.copy()

        self.contaner.clear()
        
        traverse(q)
        
        return self.contaner == arr1
        
        



    





        