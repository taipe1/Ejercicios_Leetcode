/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
  aux = []
    for(let i=1;i<=n;i++){
        if(i%3==0 && i%5==0){
            aux.push('FizzBuzz')
        }else if(i%3==0){
            aux.push('Fizz')
        }else if(i%5==0){
            aux.push('Buzz')
        }else{
            aux.push(i+"")
        }
    }
  return aux
};