class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        aux = {}
        for i in range(len(nums)):
            if nums[i] not in aux:
                aux[nums[i]]=1
            else:
                aux[nums[i]]=aux[nums[i]]+1
        num_dict = sorted(aux.items(), key = lambda x:(x[1],-x[0]))
        res = []
        for key,value in num_dict:
            res += [key]*value
        return res
        