class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        heap = []
        for key, v in count.items():
            heapq.heappush(heap, (v,key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while len(heap) > 0:
            res.append(heapq.heappop(heap)[1])
        return res

    # O(n) for building hashmap
    # O(n*log(k)) Time Heap pushes
    # Space O(k) <- Heap
    # Space O(n) <- Hashmap
    # 
    # O(n space) 
    # O(n*log*(k)) Time

"""
# Fancy Version Below


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count = collections.defaultdict(int)
        # for n in nums:
        #     count[n] += 1
        
        count = collections.Counter(nums)
        
        
        # heap = []
        # for key, v in count.items():
        #     heapq.heappush(heap, (v,key))
        #     if len(heap) > k:
        #          heapq.heappop(heap)
        # res = []
        # while len(heap) > 0:
        #     res.append(heapq.heappop(heap)[1])
        # return res

        return heapq.nlargest(k, count.keys(), key=count.get)



"""