class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        returnList = []
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char)-ord('a')] += 1
            grouped[tuple(count)].append(s)
        for s in grouped:
            returnList.append(grouped[s])
        return returnList