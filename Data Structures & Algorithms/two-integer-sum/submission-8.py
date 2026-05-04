class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        indices = []
        for i in range(len(nums)):
             numsDict[nums[i]] = i
        for i in range(len(nums)):
            print("happening1")
            print(i)
            if ((target - nums[i]) in numsDict):
                if (i != numsDict[target - nums[i]]):
                    print("happening")
                    if i > numsDict[target - nums[i]]:
                        indices.append(numsDict[target - nums[i]])
                        indices.append(i)
                    else:
                        indices.append(i)
                        indices.append(numsDict[target - nums[i]])
                    return indices
        