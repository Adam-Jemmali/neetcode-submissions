class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countxnum={}
        for num in nums:
            countxnum[num]= 1+ countxnum.get(num,0)
            #end dictionary of num/count pair

            # 1:1        (Count,num) (1,1) (2,2)  (3,3)
            # 2:2        sort by count [(1,1)    (2,2)   (3,,3)]
            # 3:3       

        arr=[]
        for num,count in countxnum.items():
            arr.append([count,num]) #to sort the count first after
        arr.sort()

        res=[]
        while len(res) <k :
            res.append(arr.pop()[1])
        return res

    
              # the lenght of neww arr smaller than k






        