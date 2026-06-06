class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res=[]

        nums.sort()

        # [ -4 , -1 ,-1 ,0,1, 2]

        for i,n in enumerate(nums):

            l=i+1 
            r=len(nums)-1

            if n ==nums[i-1] and i >0:
                continue #go next iteration  if same n and doesnt og to while loop and append it 

            while l<r:
                threesum= n + nums[l] + nums[r]
                if threesum <0 :
                    l +=1
                elif  threesum > 0:
                    r -=1
                elif threesum == 0 :
                    res.append([n,nums[l],nums[r]])
                    l +=1
                    r -=1
                    while nums [l]== nums[l-1] and l<r:
                        l =l +1
                   
        return res

                



        