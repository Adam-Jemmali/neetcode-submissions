class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setn = set()
        for i in nums:
            if i in setn:
                return True
            else:setn.add(i)
        return False

        