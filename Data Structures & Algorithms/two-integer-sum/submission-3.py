class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[1,24,5] target=25 TRUE
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] ==target:
                    return [i,j]
        return []
        