class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if not len(words) == len(pattern):
            return False
        
        mapping = dict() # key is the pattern, value is the word
        
        for i in range(len(words)):
            if pattern[i] not in mapping:
                # values() is a set - fast membership testing - O(1) amortised search
                if words[i] not in mapping.values(): 
                    mapping[pattern[i]] = words[i]
                else:
                    return False
            else:
                if not mapping[pattern[i]] == words[i]:
                    return False
        return True