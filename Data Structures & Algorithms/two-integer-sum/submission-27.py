class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3 ,4 ,5 ,6 ] t = 7 Oputput: [0,1]

        dnum_ind={}
        #set 

        for ind,num in enumerate(nums):
            diff= target - num
            if diff in dnum_ind:
                return [dnum_ind[diff],ind]

            dnum_ind[num]=ind
            

          


        
    


    
        
        