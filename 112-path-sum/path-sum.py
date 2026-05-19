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
                return None

            total += root.val

            left = FindPathSum(root.left , targetSum , total)
            if left == True:
                return True

            right = FindPathSum(root.right , targetSum , total)
            if right == True :
                return True

            if left == None and right == None and total == targetSum:
                return True 
            return False
        ans = FindPathSum(root , targetSum , 0)
        if ans == None:return False
        return ans
    
    
            




        








        

        



        