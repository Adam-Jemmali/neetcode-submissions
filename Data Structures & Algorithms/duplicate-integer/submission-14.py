class Solution:

    # [1,2,2,3] sorted: [1,1,3,5]
    # [3,4,5,3]
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False

        