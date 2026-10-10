class Solution:

    # [1,2,2,3] sorted: [1,1,3,5]
    # [3,4,5,3]
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodup= set()

        for n in nums:
            if  n in nodup:
                return True
            else:
                nodup.add(n)
        return False
        

        