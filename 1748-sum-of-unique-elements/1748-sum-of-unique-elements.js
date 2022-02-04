/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    let aux = {};
    for(let i of nums){
        aux[i]=(aux[i]||0)+1
    }
    
    let sumador = 0;
    for(let [k,v] of Object.entries(aux)){
        if(v == 1){
            sumador = sumador + parseInt(k);
        }
    }
    return sumador;
};