class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #brute force
        '''
        nums= [ 1,2,3,20]   output: 3
        '''
        res=0
       
        sett= set(nums)

        for num in nums:
            current=num
            count=0
            while current in sett:
                count += 1
                current +=1
            res= max(count, res)
        return res   #since count will be rested so pick max value cant do res= count  

