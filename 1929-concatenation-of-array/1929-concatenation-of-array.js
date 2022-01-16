/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let aux = [...nums]
    return aux.concat(nums)
    
};