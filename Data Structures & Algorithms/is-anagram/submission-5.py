class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = dict()
        letters2 = dict()
        for char in s:
         if char in t:
            letters1[char] = letters1.get(char,0) + 1
         else: 
            return False
        for char in t:
         if char in s:
            letters2[char] = letters2.get(char,0) + 1
         else:
            return False
        if letters1 == letters2:
            return True
        else: 
            return False
        