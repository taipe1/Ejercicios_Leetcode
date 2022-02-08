/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let map = {}
    for(let i of nums){
        map[i] = (map[i] || 0) + 1
    }
    return Object.entries(map).sort((a,b) => b[1] - a[1]).map( e => Number(e[0])).slice(0,k)

};