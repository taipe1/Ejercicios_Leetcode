class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        aux = word.lower()
        if(word.islower()):
            return True
        elif(word.isupper()):
            return True
        elif( word == aux[0].upper()+aux[1:]):
            return True
        else:
            return False
        
        