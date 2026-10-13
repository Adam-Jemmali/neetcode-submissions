class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # [ act, cat, ok , ko ]   OUt: [  [ act, cat], [ok,ko]    ]
         # {  tuple of the count bucket sort :  [...]}

         dituple= defaultdict(list)


         for word in strs:
            sortedstr= " "
            for letter in  sorted(word):
                sortedstr += letter
            dituple[sortedstr].append(word)
         return list(dituple.values())
           


        