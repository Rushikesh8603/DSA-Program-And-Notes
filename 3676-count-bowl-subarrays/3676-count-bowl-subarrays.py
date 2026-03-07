class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:

        bowl_count = 0
        length  = len(nums)
        stack = []

        for i in range(length-1 , -1 , -1 ):
            while stack and nums[i] > stack[-1]:
                if len(stack) >=2 :
                    bowl_count +=1
                stack.pop()

            if stack and stack[-1] > nums[i] or len(stack) == 0 :
                stack.append(nums[i])

        return bowl_count
    

    
            
        



        
        