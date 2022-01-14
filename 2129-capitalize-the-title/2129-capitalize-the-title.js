/**
 * @param {string} title
 * @return {string}
 */
var capitalizeTitle = function(title) {
    // return title.split(" ").map( e => e[0].replace(e[0],e[0].toUpperCase())+ e.slice(1)).join(" ")
    let a = title.split(" ")
    return a.map(e => {
      if(e.length >0 && e.length <=2 ){
        return e.toLowerCase()
      }else{
        return e[0].replace(e[0],e[0].toUpperCase())+ e.slice(1).toLowerCase()
      }
    }).join(" ")
};