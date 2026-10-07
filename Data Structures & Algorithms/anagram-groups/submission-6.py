class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt= defaultdict(list)
        # [ act, cat, ok , ko ]   OUt: [  [ act, cat], [ok,ko]    ]
        for word in strs:
            count= [0] * 26 
            for ch in word:
                count[ord(ch)-ord('a')] +=1
            #end word act now put in dictiiaty { count tupe : [ append the word ]}
            dictt[tuple(count)].append(word)
        #end of each word in str now return
        return list(dictt.values())
            

        
        
        
        