from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countbucket=[0] * 26
        for letter in s:
            countbucket[ord(letter)-ord('a')] +=1
        for letter in t:
            countbucket[ord(letter)-ord('a')] -=1

        for val in countbucket:
            if val != 0:
                return False
        return True
          




    
    