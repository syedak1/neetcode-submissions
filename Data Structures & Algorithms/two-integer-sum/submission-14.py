class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        numsDict = {}
        for i, n in enumerate(nums):
            print(i)
            diff = target - n
            if diff in numsDict:
                if numsDict[diff] != i:
                    indices.append(numsDict[diff])
                    indices.append(i)
                    return indices
            numsDict[n] = i
                
