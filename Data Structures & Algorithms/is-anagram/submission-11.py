from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        #dict s et t
        # s= 'a n a  '
        #t = 'naa'

        # {a:1}
        # { n :1 }


        if sorted(s)!= sorted(t):
            return False

        dicts={}
        dictt={}

        for i in range(len(s)):


            dicts[s[i]]= 1+ dicts.get(s[i],0)
            dictt[t[i]]=1+ dictt.get(t[i],0)
        return dicts==dictt
        
       



    
    