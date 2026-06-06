class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[3,4,5,6]  target = 7   OUT[ 0,1]

        theset= defaultdict(list) # value -> [indices]

        for i, n  in enumerate (nums):
            diff=target - n
            if diff in theset:
                return [ theset[diff][0]   ,i]
            theset[n].append(i)

        