class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        checked_char=set()

        #creer un set pr garder les characters 2 strings

        #ajouter les char dans le set
        # r            a c e c a r   t
        for char in t+s:
            if char  in checked_char:
                continue
            
            checked_char.add(char)

            print(checked_char)

            counts=0
            countt=0
            #prendre le count 

            for c in s:
                if c==char:
                    counts= counts+1
            for c in t:
                if c==char:
                    countt=countt+1
            if countt != counts:
                return False
        return True

        



        
        