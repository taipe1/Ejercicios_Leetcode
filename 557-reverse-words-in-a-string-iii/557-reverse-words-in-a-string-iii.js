/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return s.split(" ")
            .map( ex => ex
                          .split("")
                          .reverse()
                          .join(""))
            .join(" ")
};