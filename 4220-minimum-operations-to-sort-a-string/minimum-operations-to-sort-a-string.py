class Solution:
    def minOperations(self, s: str) -> int:

        if s == ''.join(sorted(s)):
            return 0 

        maxx = max(s)
        minn = min(s)

        if len(s) > 2:
            if s[0] == minn or s[-1] == maxx:
                return 1 
            for i in range(1 , len(s)-1):
                if s[i] == maxx or s[i] == minn:
                    print(2)
                    return 2

            return 3
            
            
        return -1
        
        
        
        