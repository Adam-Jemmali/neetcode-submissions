class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for eachs in strs:
            res += str(len(eachs)) + "#" + eachs
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

"""
input:[neet,neetc]

output  lIKE encoding: 4#neet5#neetc

so for each s in string:

in the res "" + str of len(each s)+ "#" + eachs


"""

