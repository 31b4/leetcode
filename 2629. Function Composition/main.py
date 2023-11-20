/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    if (functions.length === 0) {
        return function(x) { return x; };
    } else {
        return function(x) {
            var result = functions[functions.length - 1](x);
            for (var i = functions.length - 2; i >= 0; i--) {
                result = functions[i](result);
            }
            return result;
        };
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */
