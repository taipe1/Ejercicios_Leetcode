/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let cont = 0
    let acum = 0
    for(let i=0;i<s.length;i++){
        if(s[i] == 'L'){
            cont += 1
        }else{
            cont -= 1
        }
        if(cont == 0){
            acum = acum + 1
        }
    }
    return acum
};