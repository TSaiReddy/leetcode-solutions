function kthFactor(n, k) {
  const arr = [];
  for (let i = 1; i <= n; i++) {
    if (n % i === 0) {
      arr.push(i);
    }
  }
  return arr[k - 1] || -1;
}

console.log(kthFactor(12, 3));
console.log(kthFactor(4, 4));
console.log(kthFactor(7, 2));
