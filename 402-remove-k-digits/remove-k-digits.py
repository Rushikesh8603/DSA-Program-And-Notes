class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        length = len(num)
        stack = []
        for i in num:
            while stack and stack[-1] > i and k > 0 :
                stack.pop()
                k-=1
            stack.append(i)
                            
            if len(stack) == 1 and stack[0] == '0' :
                stack.pop()
        
        while k > 0 :
            if len(stack) > 0:
                stack.pop()
            else:break
            k-=1
        
        if not stack:
            return "0"
        return "".join(stack)
             
        





        