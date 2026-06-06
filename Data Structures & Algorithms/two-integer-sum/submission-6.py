class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #[1,24,5] target=25 TRUE
        A=[]
        for i,num in enumerate(nums):
            A.append([num,i])
        A.sort()

        

        #2p ointers  [1,5,24] A = [(1, 0), (5, 1), (24, 2)]
        i=0
        j=len(nums)-1
        while i<j:
            cursum=A[i][0] + A[j][0]
            if cursum==target:
                return [ min (A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif cursum < target:
                i +=1
            elif cursum >target:
                j -=1
        return []
        
            



     