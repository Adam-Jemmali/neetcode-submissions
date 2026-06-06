import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Split by non-alphanumeric characters and join
        chars = ''.join(re.split(r'[^A-Za-z0-9]', s)).lower()
        
        for i in range(len(chars) // 2):
            if chars[i] != chars[len(chars) - 1 - i]:  # Fixed: len(chars) - 1 - i
                return False
        return True