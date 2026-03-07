class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        if arr == sorted(arr):
            return 0

        length = len(arr)
        end = length-1
        start =  end
        for index in range(len(arr)-2 , -1 ,-1):
            if arr[index] > arr[index+1]:
                break
            start = index

        ans = length - (end - start + 1)


        def findmeindex(num):
            ans = -1
            while start <= end:
                mid = (start + end )//2
                if arr[mid] >= num:
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
        
        #tc = N*log(len(backarr))) + NlogN --- > O(NlogN)










            






        
        


        


        
        