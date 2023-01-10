class Solution(object): 
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        """

        p0 = 0
        p1 = 0
        p2 = len(nums) - 1

        while p1 <= p2:
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1
            elif nums[p1] == 1:
                p1 += 1
            else: 
                nums[p0], nums[p2], nums[p0]
                p2 -= 1


