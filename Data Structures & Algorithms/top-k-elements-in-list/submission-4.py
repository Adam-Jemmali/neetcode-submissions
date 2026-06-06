class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ''' 
 nums = [1,2,2,3,3,3], k = 2   [2,3]

    after dic  { 1:1 ,2:2  3:3}
        '''
        dic={}
        for i in nums:
            dic[i]= 1+ dic.get(i,0)
        arr=[]
        for num,counter in dic.items():
            arr.append([counter,num])
        arr.sort()
        resultat=[]
        while len(resultat) < k:
            resultat.append(arr.pop()[1])
        return resultat

            
        