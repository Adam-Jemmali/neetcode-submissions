class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums=[1,1,1,2,2,3]  k=2  OUTPUT [3,2]
        
        dict_count= {}
        for num in nums:
            dict_count[num]= 1+ dict_count.get(num,0)
        #{1:3     2:2    3:1}
        A=[]

        for num,count in dict_count.items():
            A.append([count,num]) # A= [  [3,1]   [2,2]      [1,3]   ]
        A.sort() # A= [ (count,num) [1,3]    [2,2]    [3,1]     ]

        resultat=[]
        for i in range(len(A)-1, -1, -1):
            resultat.append(A.pop()[1])
            if len(resultat)==k:
                return resultat



      

        
     


       
        



        