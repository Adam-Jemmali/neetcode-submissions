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
        while len(resultat)<k:
             resultat.append(A.pop()[1])
        return resultat

    


      

        
     


       
        



        