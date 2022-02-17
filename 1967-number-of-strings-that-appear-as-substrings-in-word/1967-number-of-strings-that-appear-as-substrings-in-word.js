/**
 * @param {string[]} patterns
 * @param {string} word
 * @return {number}
 */
var numOfStrings = function(patterns, word) {
    return patterns.map(e => word.includes(e))
                                      .reduce((a,b) => a+b,0)
};