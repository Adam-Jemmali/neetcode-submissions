class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            dict1={}
            for n in nums:

                dict1[n]=1+dict1.get(n,0)

            arr=[]
            for num,count in dict1.items():
                arr.append([count,num])
                arr.sort()
            resultat=[]
            for i in range(k):
                resultat.append(arr.pop()[1])
            return resultat
            


                

            #[  [1,1]  [2,2]  , [3,3]] we are returning the numbers

        