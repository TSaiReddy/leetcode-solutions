function romanToInt(s) {
  const hash = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };

  let result = 0;

  for (let i = 0; i < s.length; i++) {
    const curVal = hash[s[i]];
    const nextVal = hash[s[i + 1]];
    if (curVal < nextVal) {
      result -= curVal;
    } else {
      result += curVal;
    }
  }

  return result;
}

console.log(romanToInt("III"));
console.log(romanToInt("LVIII"));
console.log(romanToInt("MCMXCIV"));
