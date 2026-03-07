class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        length  = len(heights)
        rightSum =[0] * length
    

        def giveLeftSum():
            stack = []
            leftSum = [0] * length 
            for i in range(length):
                while stack and heights[stack[-1][0]] >= heights[i]:
                    stack.pop()
                if not stack:
                    Total_length = i+1
                    totalSum = Total_length * heights[i] 
                    leftSum[i] = totalSum
                    stack.append([i ,leftSum[i]])
                else:
                    leftSum[i] = (heights[i] * (i - stack[-1][0])) + stack[-1][1] 
                    stack.append([i , leftSum[i]])
            return leftSum

        def giveRightSum():
            stack = []
            rightSum =[0] * length
            for i in range(length-1 , -1 , -1):
                while stack and heights[stack[-1][0]] >= heights[i]:
                    stack.pop()
                if not stack:
                    Total_length = length - i 
                    totalSum = Total_length * heights[i] 
                    rightSum[i] = totalSum
                    stack.append([i ,rightSum[i]])
                else:
                    rightSum[i] = heights[i] *( stack[-1][0] - i ) +  stack[-1][1]
                    stack.append([i , rightSum[i]])
            return rightSum
        

        leftSum = giveLeftSum()
        rightSum = giveRightSum()
        print(rightSum)
        print(leftSum)

        maxSum = 0 

        for i in range(length):
            if i == 0 :
                maxSum = max(maxSum,rightSum[i])
            else:
                maxSum = max(maxSum, leftSum[i-1] + rightSum[i])
        
        return maxSum

    

        



            

            

            













        