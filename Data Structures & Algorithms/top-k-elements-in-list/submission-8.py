class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums=[1,1,1,2,2,3]  k=2  OUTPUT [3,2]
        #  { 1:3  2:2 3:1}
        #a=[ [3,1] , [2,2] [1,3] ]
        #a.sort = [   ]
        

        dictt= {}
        
        for num in nums:
            dictt[num]= 1 + dictt.get(num,0)
        A=[]
        for num,count in dictt.items():
            A.append([count,num]) # [   [1,1] [2,2]  [3,3] (right has more COUNT)
        A.sort()

        res = []

        for i in range(k):
            res.append(A.pop()[1])
        return res


       
        



        