function isHappy(n) {
  const hash = new Set();

  function recu(current) {
    if (current === 1) return true;
    if (hash.has(current)) return false;
    hash.add(current);

    let result = 0;
    for (const value of String(current)) result += value * value;
    return recu(result);
  }
  return recu(n);
}
console.log(isHappy(19));
console.log(isHappy(2));
