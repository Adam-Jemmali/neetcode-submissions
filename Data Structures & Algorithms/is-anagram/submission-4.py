class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic ,dic2= {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            #store value of dif charact in string {key.value}
            dic[s[i]]= 1+ dic.get(s[i],0)
            dic2[t[i]]= 1+ dic2.get(t[i],0)
        return dic==dic2


      


#rac =s 
#car =t 

