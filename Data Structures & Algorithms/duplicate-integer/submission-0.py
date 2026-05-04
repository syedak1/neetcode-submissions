class Solution:    
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict.fromkeys(nums, 0)
        for i in nums :
            if i in hashmap :
                hashmap[i] += 1
                if hashmap[i] >= 2 :
                    return True
        return False        
