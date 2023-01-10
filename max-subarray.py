class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Code with defense in mind just in case it is 0 
        if len(nums) == 0:
            return 0
        res = nums[0]
        currMax = 0
        for n in nums:
            # Code the logic if less than zero etc 
            if currMax + n < 0:
                currMax = 0
                res = max(n, res)
            else:
                currMax += n
                res = max(currMax, res)
            return res

