/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    aux = 0
    for(let i=0; i < sentences.length ; i++){
        if(aux < sentences[i].split(" ").length){
          aux = sentences[i].split(" ").length;
        }
    }
    return aux;
};