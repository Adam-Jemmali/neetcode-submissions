class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictt={}
        for n in nums:
            dictt[n]=dictt.get(n,0) +1 

        # {1:1 ,3:2 , 4:3}  { num:count}

        restempo=[]
        for num,count in dictt.items():
            restempo.append([count,num])
        restempo.sort()
        #[ [1,1],[3,2],[4,3]   ]  POP the last elements

        res=[]

        while len(res) <k:
            res.append(restempo.pop()[1])
        #since if k=2 0 1 cant count 2 so < k 
        return res

            


        