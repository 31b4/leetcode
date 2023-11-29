var once = f => (...a) => f ? [f(...a), f=undefined][0] : f
