class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        if arr == sorted(arr):
            return 0
        length = len(arr)
        backarr = []

        for index in range(len(arr)-1 , -1 ,-1):
            if backarr and arr[index] > backarr[-1]:
                break
            backarr.append(arr[index])

        backarr.reverse() # this reverse it in a inplace. 

        ans = length - len(backarr)

        print(backarr)

        def findmeindex(num):
            start , end = 0 , len(backarr)-1
            ans = -1
            while start <= end:
                mid = (start + end )//2
    
                if backarr[mid] >= num:
                    ans = mid
                    end = mid -1
                else:
                    start = mid+1
            return ans 

        for i in range(len(arr)):
            if i > 0 and arr[i] < arr[i-1]:
                break
            index = findmeindex(arr[i])
            print(index)
            if index != -1:      
                leftside_element = len(backarr) - index # count of left side elemnts 
                ans = min(ans , length - (leftside_element + i+1))

            else:
                ans = min(ans , length - (i+1))
        return ans 
        








            






        
        


        


        
        