class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [ 1 ,2 ,3 ,4 ] '''


        '''  [1,2,3,4]

        MULTIPLCIATIONS BEFORE INDEX 
         [1 ,1 ,2,6]

         for i in range ((1,n)) 



        '''
        prefix=1

        resarr= [1] * len (nums)

        for i in range(len(nums)):
            resarr[i]= prefix
            prefix= nums[i] * prefix

        postfix=1

        for i in range (len(nums)-1,-1, -1):
            resarr[i]= postfix * resarr[i]
            postfix= postfix * nums[i]
        return resarr
            


        