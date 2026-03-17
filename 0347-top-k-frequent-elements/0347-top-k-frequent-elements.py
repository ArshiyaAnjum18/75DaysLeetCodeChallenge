class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        
      
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        
        n = len(nums)
        buckets = [[] for _ in range(n + 1)] 
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
       
        res = []
        for i in range(n, 0, -1):  
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res