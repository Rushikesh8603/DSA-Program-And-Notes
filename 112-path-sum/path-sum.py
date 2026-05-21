# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def FindPathSum(root ,targetSum, total):

            if root == None:
                return False

            total+=root.val

            if root.left == None and root.right == None:
                if total == targetSum:
                    return True
                else:
                    return False

            left = FindPathSum(root.left, targetSum , total)
            
            right = FindPathSum(root.right, targetSum , total)

            return left or right

        return FindPathSum(root, targetSum , 0)
    


            
        


    

            
    
    
            




        








        

        



        