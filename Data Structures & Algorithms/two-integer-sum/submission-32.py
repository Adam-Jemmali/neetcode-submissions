class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # [3 ,4 ,5 ,6 ] t = 7 Oputput: [0,1]
        # [1,1,2] t=2

        dictt ={}
       
        for i,n in enumerate(nums):

            dictt[n]=i  # {1:0, 1:1 , 2:2}
        
        for i,n in enumerate(nums):
            numbertoadd= target -n
            if numbertoadd in dictt and dictt[numbertoadd]!=i  :
                return[i,dictt[numbertoadd]]
        return []
        
    

