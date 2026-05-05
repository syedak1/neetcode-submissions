class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        usednums = {}
        listednums = defaultdict(list)
        returnvals = []
        for s in nums:
            if s in usednums:
                usednums[s] += 1
            else: 
                usednums[s] = 0

        for s in usednums:
            listednums[usednums[s]].append(s)
            
        count = len(nums) - 1
        while k > 0:
            if len(listednums[count]) > 0 :
                for s in listednums[count]:
                    returnvals.append(s)
                    k = k - 1
            count = count - 1
        return returnvals
                
                

        

