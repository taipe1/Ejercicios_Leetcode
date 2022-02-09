/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let maximo = Math.max(word1.length, word2.length)
    let cad = ''
    for(let i=0;i<maximo;i++){
        cad = cad + (word1[i] || '') + (word2[i] || '')
    }
    return cad
};