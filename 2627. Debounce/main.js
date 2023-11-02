var debounce = function(fn, t) {
    let id;
    return function(...args) {
        clearTimeout(id);
        id = setTimeout(() => fn(...args),t); 
    }
};
