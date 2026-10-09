class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictt= defaultdict(list)
        # [ act, cat, ok , ko ]   OUt: [  [ act, cat], [ok,ko]    ]

        # {  tuple of the count bucket sort :  [...]}

        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord('a')] +=1 
            dictt[tuple(count)].append(word)
        return list(dictt.values())

        


        

        
        
        