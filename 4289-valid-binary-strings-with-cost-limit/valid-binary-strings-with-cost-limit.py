class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:

        arr = ["0"] * n 
        ans = []
        def subseq(i , arr , count):
            if i >= n :
                if count <= k :
                    ans.append(arr.copy())
                return 
            if i < n-1 and arr[i] == arr[i+1] and arr[i] == "1":
                return 

            arr[i] = "1"
    
            count += i 

            subseq(i+1 , arr, count )
            arr[i] = "0"
            count -= i 
            subseq(i+1 , arr, count)

        subseq(0 , arr , count = 0)

        finalseb = []

        for i in ans:
            flag = True
            for x in range(len(i)-1):
                if i[x] == '1' and i[x+1] == '1' :
                    flag = False;break

            if flag :
                finalseb.append("".join(i))
        return finalseb





        




        
        