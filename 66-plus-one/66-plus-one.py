class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = ''
        for i in digits:
            c = c + str(i)
        t = int(c) + 1
        return str(t).replace(""," ").split()
        