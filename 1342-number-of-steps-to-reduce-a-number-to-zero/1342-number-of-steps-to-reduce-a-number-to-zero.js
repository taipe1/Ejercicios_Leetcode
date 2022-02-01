/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let cont = 0
    while(num >0){
          if(num%2==0){
            // console.log(num)
              cont ++;
              num = Math.round(num/2);
          }else{
            // console.log(num)
              cont ++;
              num = num - 1;
          }
    }
    return cont;
};