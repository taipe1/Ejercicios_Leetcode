/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    let cont = 0;
    for(let i = low; i <= high ; i++){
        if(i%2 == 1){
            cont = cont + 1;
        }
    }
    return cont
};