class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt= {}
        for ind,num in enumerate(nums):
            dictt[num]=ind
        


        for ind,num in enumerate(nums):
            difference= target-num
            if  difference in dictt and ind != dictt[difference]:
                return[ind,dictt[difference]]
        return []


        # [nums=[1,3,4,2] t =6
       


       
        
    

