/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    for(let i = 0; i< 100; i++){
        if(Math.pow(4,i) === n){
            return true
        }
    }
    return false
};