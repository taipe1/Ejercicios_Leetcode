/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    let aux = 0
    items.map (e => {
        switch(ruleKey){
            case 'type':
                e[0] == ruleValue && aux++;
                break;
            case 'color':
                e[1] == ruleValue && aux++;
                break;
            case 'name':
                e[2] == ruleValue && aux++;
                break;
        }
    })
    return aux;
};