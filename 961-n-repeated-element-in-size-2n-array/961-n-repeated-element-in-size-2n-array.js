/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(A) {
    let dic = {}

    for(let i = 0; i < A.length; i++){

        if(A[i] in dic) return A[i]

        dic[A[i]] = 0
    }    
};