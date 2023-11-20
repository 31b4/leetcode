/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var arr2 = []
    for (let i = 0; i < arr.length; i++) {
        if(fn(arr[i],i)){
            arr2.push(arr[i])
        }
    }
    return arr2
};
