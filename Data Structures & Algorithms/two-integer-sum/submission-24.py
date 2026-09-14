class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3 ,4 ,5 ,6 ] t = 7 Oputput: [0,1]

        dnum_ind={}

        for ind,num in enumerate(nums):
            dnum_ind[num]=ind # { 3:0 , 4:1 , 5:2 , 6:3}

        for ind,num in enumerate(nums):
            diff= target-num
            #make sure diff in dictionnary AND VERY IMPORTANT ITS NOT THE SAME INDEX BCS IT WILL RETURN THE SAME NUMBER 3 +3 WHICH WILL OUTPUT [1,1] nums=[1,3,4,2] 
            if diff in dnum_ind and dnum_ind[diff] != ind:
                return [ind,dnum_ind[diff]]
        return []




        
    


    
        
        