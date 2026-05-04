class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        returnVals = []
        for i in range(len(nums)):
            numsDict[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in numsDict:
                if i != numsDict[target - nums[i]]:
                    if i > numsDict[target - nums[i]]:
                        returnVals.append(numsDict[target - nums[i]])
                        returnVals.append(i)
                    returnVals.append(i)
                    returnVals.append(numsDict[target - nums[i]])
                    return returnVals
                    

        
        