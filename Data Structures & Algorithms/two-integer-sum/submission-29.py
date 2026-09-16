class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3 ,4 ,5 ,6 ] t = 7 Oputput: [0,1]
        # [1,3,4,2] t= 6 O:

        dictt={}
        for ind,n in enumerate(nums):
            dictt[n]=ind
        #set is done now { 1:0, 3:1, 4:2, 2:3}
        for ind,n in enumerate(nums):
            diff= target -n
            if diff in dictt and dictt[diff] !=ind:
                return [ind, dictt[diff]]
        return []


        
        

          


        
    


    
        
        