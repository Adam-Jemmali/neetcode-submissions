from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #dict s et t
        # s= 'a n a  '
        #t = 'naa'

        if len(s) != len(t):
            return False

        countlist= [1] * 26

        for i in range(len(s)):
            #start with s string with ord function 
            #ord will return [index of the alaphabe letter]
            countlist[ord(s[i])- ord('a')] += 1
            countlist[ord(t[i])- ord('a')] -= 1
        
        print(countlist)
        for value in countlist:
            if value != 1:
                return False
        return True
        

