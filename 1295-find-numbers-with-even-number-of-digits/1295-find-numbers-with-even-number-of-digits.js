/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let aux = nums.map(e => e.toString().length).filter(a => a%2==0).length
    return aux
};