class Solution: 
    def checkPossibility(self, nums: List[int]) -> bool:
        idx = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # if there's two dip or more
                if idx is not None:
                    return False
                idx = i
            # if there's no dip
            if idx is None:
                return True 
            # if there's only dip 
            if idx == 0:
                return True
            if idx == len(nums) - 2:
                return True
            if nums[idx] <= nums[idx + 2]:
                return True
            if nums[idx - 1] <= nums[idx + 1]:
                return True
            return False

            
                  