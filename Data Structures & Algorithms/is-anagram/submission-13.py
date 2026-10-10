from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        countbucket=[0] * 26
        countbucket2=[0]*26
        for letter in s:
            countbucket[ord(letter)-ord('a')] +=1
        for letter in t:
            countbucket2[ord(letter)-ord('a')] +=1

        return tuple(countbucket)==tuple(countbucket2)
        




    
    