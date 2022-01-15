class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        cade = ''
        aux = s.split()
        c = 0
        for i in range(len(aux)):
            cade += ' ' + aux[i]
            c += 1
            if(c == k):
                break
        return cade[1:]
        