function climbStairs(n) {
  let i = 2;
  let prev = 1;
  let prePrev = 1;
  if (n == 1) {
    return 1;
  } else if (n == 2) {
    return 2;
  } else {
    while (i < n) {
      const current = prePrev + prev;
      prePrev = prev;
      prev = current;
      i++;
    }
  }
  return prePrev + prev;
}

console.log(climbStairs(6));
