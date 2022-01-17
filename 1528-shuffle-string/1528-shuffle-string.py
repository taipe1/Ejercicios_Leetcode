class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        aux = [""]*len(s)
        for key,value in enumerate(indices):
            aux[value] = s[key]
        return "".join(aux)
        