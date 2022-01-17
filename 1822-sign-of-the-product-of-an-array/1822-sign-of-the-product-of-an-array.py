class Solution:
    def arraySign(self, nums: List[int]) -> int:
        produc = 1
        for i in range(len(nums)):
            if(nums[i]>0):
                produc = produc * (1)
            elif(nums[i]<0):
                produc = produc * (-1)
            else:
                produc = produc * (0)
        return produc
                
        