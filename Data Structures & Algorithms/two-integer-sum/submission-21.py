class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3 ,4 ,5 ,6 ] t = 7 Oputput: [0,1]
        A=[]
        for ind,num in enumerate(nums):
            A.append([num,ind])
        #cant sort infex so make sure its num before
        A.sort()

        i=0
        j=len(nums)-1
        # [ -5 ,-4,-3,-2,-1] t=-8
        #-6 then if decrement j -7 is smaller everything true

        while i<j:
            tempnum= A[i][0] + A[j][0]
            if tempnum == target:
                #make sure the pair of indices are INCREASING ORDER
                return [min(A[i][1],A[j][1]), max(A[i][1],A[j][1]) ]
            elif tempnum < target:
                i +=1
            else: 
                j -=1
        return []

        
        