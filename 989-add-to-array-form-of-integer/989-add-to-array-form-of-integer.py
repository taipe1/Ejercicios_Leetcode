class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        cade = ''
        for i in num:
            cade += str(i)
        return list(str(int(cade)+k))
        
        