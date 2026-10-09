class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictt= defaultdict(list)
        # [ act, cat, ok , ko ]   OUt: [  [ act, cat], [ok,ko]    ]

        # {  sortedword :  [...]}

        for word in strs:
            sortedconstantword= ""
            for lter in sorted(word):
                sortedconstantword +=lter
            dictt[sortedconstantword].append(word)
        return list(dictt.values())

        

        
        
        