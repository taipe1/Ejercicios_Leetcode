/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
  let aux = 0
  let c=0
  for(let i=0;i<nums.length;i++){
    if(nums[i]==1){
      c++;
    }else{
      c=0
    }
    aux = Math.max(c,aux)
  }  
  return aux
};