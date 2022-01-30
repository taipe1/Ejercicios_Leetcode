/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParity = function(nums) {
    let aux1 = []
    let aux2 = []
    for(let i=0;i<nums.length;i++){
        if(nums[i]%2==0){
            aux1.push(nums[i])
        }else{
            aux2.push(nums[i])
        }
    }
    return [...aux1,...aux2]
}