class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a set
        setd= set()
        for n in nums:
            if n in setd:
                return True

            else:
                setd.add(n)
        return False
        