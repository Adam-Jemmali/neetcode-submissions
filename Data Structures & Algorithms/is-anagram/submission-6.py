class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics,dic_t={}, {}
        #put 2 dictinoaires
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            dics[s[i]]=1+dics.get(s[i],0)
            dic_t[t[i]]=1+dic_t.get(t[i],0)
        return dics==dic_t
        