class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        delete = ''
        for i in range(len(s)):
            delete = delete + s[i]
            if part in delete:
                delete = delete.replace(part,'')
        return (delete)
        
        