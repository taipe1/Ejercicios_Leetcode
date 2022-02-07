class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[l]=nums[i]
                l += 1
        for i in range(l,len(nums)):
            nums[i] = 0
        return nums
        