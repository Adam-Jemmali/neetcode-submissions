class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,2,3] t=6 COPY ARRAY   { 3:0  , 2:1 , : ,}

        dictt= {}

        for i, n in enumerate(nums):
            difference= target -n
            if difference in dictt:
                return [  dictt[difference],i]
            dictt[n]=i

       

        
        