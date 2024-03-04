function memoize(fn) {
  const cache = new Map();
  return function() {
    let key = arguments[0];
    if (arguments[1]) {
      key += arguments[1] * 100001;
    }
    const result = cache.get(key);
    if (result !== undefined) {
      return result;
    }
    const functionOutput = fn.apply(null, arguments);
    cache.set(key, functionOutput);
    return functionOutput;
  }
}
