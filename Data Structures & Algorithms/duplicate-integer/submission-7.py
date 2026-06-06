class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        settest=set()

        for i in nums:
            if i in settest:
                return True
            else:
                settest.add(i)
        return False
            
        # [1,2,3,4]

        