// Normal Approach
function fib(n) {
  if (n === 0) return 0;
  if (n === 1) return 1;

  return fib(n - 2) + fib(n - 1);
}

// Top down Approach
function fib(n) {
  const hash = { 0: 0, 1: 1 };

  function f(x) {
    if (x in hash) return hash[x];
    else {
      hash[x] = f(x - 1) + f(x - 2);
      return hash[x];
    }
  }
  return f(n);
}

// Bottom up Approach
function fib(n) {
  const dp = Array(n).fill(0);
  dp[0] = 0;
  dp[1] = 1;

  for (let i = 2; i < n + 1; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
}

// Bottom up Approach (optimized)
function fib(n) {
  if (n === 0) return 0;
  if (n === 1) return 1;

  let lastButOne = 0;
  let last = 1;

  for (let i = 2; i < n + 1; i++) {
    const temp = lastButOne;
    lastButOne = last;
    last = last + temp;
  }

  return last;
}

console.log(fib(n));
