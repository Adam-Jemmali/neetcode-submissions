class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #nums=[1,1,1,2,2,3]  k=2  OUTPUT [3,2]
        #  { 1:3  2:2 3:1}
        dict_count= {}
        freq= [ [] for i in range(len(nums)+1)] # must include + 1 si

        for n in nums:
            dict_count[n]= 1+ dict_count.get(n,0)
        
        for n,count in dict_count.items():
            freq[count].append(n) # [[],[3],[2] ,[1],[],[],[]]
        resultat=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                resultat.append(num)
                if len(resultat)==k:
                    return resultat          
           

        
     


       
        



        