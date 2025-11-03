class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        
        heap = []
        for key, val in freq.items(): 
            heapq.heappush(heap, (-1*val, key))
        # print(heap)
        res = [] 
        for i in range(k): 
            res.append((heapq.heappop(heap))[1])
        return res 