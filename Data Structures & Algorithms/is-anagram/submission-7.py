class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for char in s:
            if char not in sDict:
                sDict[char] = 0
            else :
                sDict[char] = sDict[char] + 1
        for char in t:
            if char not in tDict:
                tDict[char] = 0
            else: 
                tDict[char] = tDict[char] + 1
        print("tdict" , tDict)
        print("sdict", sDict)
        return tDict == sDict
                
