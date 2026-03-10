class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        MAX , MIN = 0 , length+1
        need = False
        stack = []

        for i in range(length):
            if not stack:
                stack.append(i)
            elif nums[i] > nums[stack[-1]]:
                    stack.append(i)
        start = len(stack)-1


        print(stack)
        for i in range(length-1, -1 , -1):
            print(start , i )
            while start >= 0 and (stack[start] > i or nums[stack[start]] > nums[i]):
                if nums[stack[start]] > nums[i] and stack[start] <= i:
                    need = True
                    MAX = max(MAX , i , stack[start])
                    MIN = min(MIN , i , stack[start])

                start -=1

        print(MAX, MIN)
        if need:
            return (MAX-MIN)+1
        return 0

#nums =
# [2,3,3,2,4]. # use this test case next time for solving. 