class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3 ,4 ,5 ,6 ] t = 7 Oputput: [0,1]
        # [1,3,4,2] t= 6 O:

       dictt ={}

       for i,n in enumerate(nums):
        diff= target-n
        if diff in dictt:
            return [dictt[diff],i]
        dictt[n]=i
        