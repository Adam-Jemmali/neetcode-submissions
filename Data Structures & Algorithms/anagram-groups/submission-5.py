class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultat= defaultdict(list)  # {  : []}
        for s in strs:
            count= [0] * 26 #create a list of 0 values to put 1 for values in the letters
            for c in s:
                # each letter and put it to index value with +1
                count[ord(c)- ord('a')] += 1 
            resultat[tuple(count)].append(s)
        return list(resultat.values()) 


        