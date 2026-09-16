class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3 ,4 ,5 ,6 ] t = 7 Oputput: [0,1]
        # [1,3,4,2] t= 6 O:

        #sort the Array in new array then  keep their ORIGINAL ARRAYindices even after sorting
        A=[]

        for ind,n in enumerate(nums):
            A.append([n,ind])
        
        A.sort()
        #[[3, 0], [4, 1], [5, 2], [6, 3]]
        

        i=0
        j=len(nums)-1

        while i<j:
            current=A[i][0] + A[j][0]

            if current == target :
                return [min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
            elif current < target:
                i +=1
            else:
                j-=1
        return []
        
    
            
            





        
        

          


        
    


    
        
        