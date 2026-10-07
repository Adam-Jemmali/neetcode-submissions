class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt= defaultdict(list)
        # [ act, cat, ok , ko ]   OUt: [  [ act, cat], [ok,ko]    ]
        for word in strs:
            sortedword=""
            for ch in sorted(word):
                sortedword += ch
            dictt[sortedword].append(word)
        return list(dictt.values())
        
        
        
        