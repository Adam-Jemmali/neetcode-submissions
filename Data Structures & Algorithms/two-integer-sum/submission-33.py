class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # [4,5,6 ] t = 10 Oputput: [0,2]
        # [1,1,2] t=2

        dictt ={}
        # {1:0, 1:1 , 2:2}
        # {4:0, 5:1, 6:2}  #trace  { 4:0  THEN ADDING 5:1  THEN CHECK NUMBER IN DICTT}
        
        for i,n in enumerate(nums):
            numbertoadd= target -n
            if numbertoadd in dictt:
                return[dictt[numbertoadd],i]
            dictt[n]=i
        
        
    

