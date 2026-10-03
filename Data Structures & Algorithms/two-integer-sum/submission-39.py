class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # [1,3,5]
        # [1,1,2] t=2
        #nums=[-1,-2,-3,-4,-5] target = -8 OUTPUT [ 2 ,4]
        #sorted: [-5,-4,-3,-2,-1]


        A=[]

        for i,n in enumerate(nums):
            A.append([n,i]) # [[3,0], [5,1],[ 1,2]]

        A.sort() #very impor.tant to sort if no sort if j-- NEVER RETURNING SOMETHING WE RETURN ALWAYS [] SINCE 

        i=0
        j= len(nums)-1
        while i<j:
            number= A[i][0] + A[j][0]
            if number ==target:
                return [ min(A[i][1], A[j][1]),max(A[i][1], A[j][1])]
            elif number < target:
                i +=1
            else:
                j -=1
        return [] # it wil ALWAYS BE BIGGER SO WONT 
        
        
            






       
        
    

