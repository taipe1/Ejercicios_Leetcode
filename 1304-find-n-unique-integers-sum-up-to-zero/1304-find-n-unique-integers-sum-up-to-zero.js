/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    let auc = []
    if(n%2!=0){
        auc.push(0)
    }
    while(auc.length < n){
        let temp = auc.length + 1
        auc.push(temp)
        auc.push(-temp)
    }
    return auc
    
};