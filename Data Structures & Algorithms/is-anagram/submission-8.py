class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #baes case not anagram if diff len strings:
        if len(s) != len(t):
            return False
        return sorted(s)==sorted(t)
        