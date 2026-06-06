class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        count=1
        consecutive=1
        #2,3,4,4,5,10,2
        for i in range(len(nums)-1):

            if nums[i]+1 ==nums[i+1]:
                count=count+1
                consecutive=max(count,consecutive)
            elif nums[i]==nums[i+1]:
                continue
            else:
                count=1
                consecutive=max(count,consecutive)
        return consecutive
        

                



    
        