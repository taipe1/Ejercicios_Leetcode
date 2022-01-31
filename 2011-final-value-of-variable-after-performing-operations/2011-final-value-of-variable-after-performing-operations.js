/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let cont = 0
    for(let i=0;i<operations.length;i++){
        if( (operations[i]=='--X') || (operations[i]=='X--') ){
            cont = cont - 1;
        }else{
            cont = cont + 1;
        }
    }
    return cont
};