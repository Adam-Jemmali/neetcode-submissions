class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        #[2,20,4,10,3,4,5]

        for num in  nums:
            cons=0
            current=num
            while current in numSet:
                cons +=1
                current= current + 1
            res= max(cons,res)  # cant do res=cons since it will override cons value very iteration
        return res
