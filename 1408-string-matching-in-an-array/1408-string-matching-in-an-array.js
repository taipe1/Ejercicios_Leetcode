/**
 * @param {string[]} words
 * @return {string[]}
 */
var stringMatching = function(words) {
    let sol = [];
    words.sort((a, b) => a.length - b.length);
    for (let i = 0; i < words.length - 1; i++) {
        let filter = words.slice(i + 1).filter( word => word.includes(words[i]));
        if(filter.length){
          sol.push(words[i])
        }
    }
    return sol
};