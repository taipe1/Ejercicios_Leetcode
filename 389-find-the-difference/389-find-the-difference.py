class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l1 = sorted(s)
        l2 = sorted(t)
        
        try:
            for i in range(len(l2)):
                if l1[i] != l2[i]:
                    return l2[i]
        except:
            return l2[len(l2)-1]