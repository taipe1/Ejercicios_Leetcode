/**
 * @param {number} num
 * @return {boolean}
 */
var checkPerfectNumber = function(num) {
    let contador = 0;
    for(let i =1;i<num;i++){
        if(num%i ==0){
            contador += i
        }
    }
    if(contador === num){
        return true
    }
    else{
        return false
    }
};