class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #set defaultdict {key"[]}
        resultat=defaultdict(list)
        for i in strs:
            #join sub strings with this ["act","pots","tops","cat","stop","hat"]
            sortedstr=''.join(sorted(i))
            resultat[sortedstr].append(i)
        return list(resultat.values())
        


        
        