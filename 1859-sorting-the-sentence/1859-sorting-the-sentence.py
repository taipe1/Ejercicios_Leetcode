class Solution:
    def sortSentence(self, s: str) -> str:
        aux = s.split()
        diccionario = {}
        cadena = ''
        for i in aux:
            diccionario[i[-1]] = i[:-1]
        for j in sorted(diccionario):
            cadena = cadena+' ' + diccionario[j]
        return cadena[1:]
        