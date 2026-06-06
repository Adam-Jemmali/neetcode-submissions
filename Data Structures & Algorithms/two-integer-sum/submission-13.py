class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,2,3] t=6 COPY ARRAY  [0,2]
        A =[]
        for i,n in  enumerate(nums):
            A.append([n,i])
        # [  [2,1] [3,0] , [3,2]]
        A.sort()

        #
        i=0 
        j= len(nums) -1 
        
        while i<j:
            somme= A[i][0]+ A[j][0]
            if somme== target:
                return [ min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
            elif somme < target:
                i +=1
            else:
                j -=1
        return []


        
        