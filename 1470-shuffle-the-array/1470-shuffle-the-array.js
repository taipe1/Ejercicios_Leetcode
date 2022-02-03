/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    let aux = []
    for(let i =0; i<n ;i++){
        aux.push(nums[i],nums[n+i])
    }
    return aux
};