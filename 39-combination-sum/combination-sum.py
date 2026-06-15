class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.ans = []
        arr = []
        n = len(nums)
        def uniqueCombi(i , summ ):
            if i >= n or summ > target:
                return 
            if summ == target:
                self.ans.append(arr.copy())
                return 

            summ+= nums[i]
            arr.append(nums[i])
            uniqueCombi(i , summ)
            summ-=nums[i]
            arr.pop()
            uniqueCombi(i+1 , summ)
        
        uniqueCombi(0 , 0)

        return self.ans
    



            




        