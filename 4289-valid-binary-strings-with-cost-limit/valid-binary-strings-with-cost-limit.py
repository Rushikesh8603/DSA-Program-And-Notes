class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:

        arr = ["0"] * n 
        ans = []
        def subseq(i , arr , count):
            if i >= n :
                if count <= k :
                    ans.append("".join(arr))
                return 

            arr[i] = '0'
  


            subseq(i+1 , arr, count )
            
            if i==0 or arr[i-1] == '0':
                arr[i] = '1'
                count += i
                subseq(i+1 , arr, count)
                arr[i] = '0'

        subseq(0 , arr , count = 0)

        return ans

    