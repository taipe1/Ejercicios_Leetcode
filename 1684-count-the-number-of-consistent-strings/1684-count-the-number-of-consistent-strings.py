class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cont = 0
        for i in words:
            for j in i:
                if j not in allowed:
                    print(j)
                    cont += 1
                    break
        return len(words) - cont