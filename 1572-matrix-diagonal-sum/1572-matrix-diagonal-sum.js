/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function(mat) {
    let suma = 0
    for(let i=0;i<mat.length;i++){
        for(let j=0;j<mat[i].length;j++){
            if( (i == j) || ( (i+j) == mat[i].length - 1 ) ){
                suma = suma + mat[i][j]
            }
        }
    }
    return suma
};