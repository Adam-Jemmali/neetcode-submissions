class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6] t=4)=7
        dictt1= {}
        for i, n in enumerate (nums):
            difference= target-n
            if difference in dictt1:
                return [dictt1[difference],i] # the value of  KEY difference and I(current number)
            dictt1[n]=i # n is key i is value eg. { 3:0 }

        
        