class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = 0
        for i in nums:
            if(i == 0):
                c = c + 1
                if(c == 2):
                    return True
        return sum(set(nums)) != sum(nums)
        
        
        