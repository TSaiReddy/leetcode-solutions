function getLucky(s, k) {
  const alphabetValues = {};

  for (let i = 0; i < 26; i++) {
    const letter = String.fromCharCode(97 + i);
    alphabetValues[letter] = i + 1;
  }

  let sToValues = "";

  for (const char of s) {
    sToValues += alphabetValues[char];
  }

  for (let i = 0; i < k; i++) {
    let subResult = 0;
    for (let j = 0; j < sToValues.length; j++) {
      subResult += Number(sToValues[j]);
    }
    sToValues = String(subResult);
    subResult = 0;
  }

  return sToValues;
}

console.log(getLucky("leetcode", 2));
