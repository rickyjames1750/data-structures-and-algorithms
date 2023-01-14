class Solution: 
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1])) # O(nlohn)
        res = []
        for p in people: # O(n)
            res.insert(p[1], p) # O(n)
        return res

    # Time Complexity O(N^2)
    # Space : O(N)