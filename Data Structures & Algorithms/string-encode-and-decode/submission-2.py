class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        resencode=""
        #example  input:[neet,neetc] output: 4#neet5#neetc

        for each in strs:
            resencode= resencode+ str(len(each))+"#" + each
        return resencode


    def decode(self, s: str) -> List[str]:
        ''' s=4#neet5#neetc       --> [neet,neetc]

        '''
        res=[]
        i=0
        while i < len(s):
            k=i
            while s[k]!="#":
                k += 1
            #reached number now convert str to  int value
            lengthword= int(s[i:k])
            i=k+1 #go after # index
            k= i+lengthword
            res.append(s[i:k])
            i=k #put i pointer to k 
        return res




        

