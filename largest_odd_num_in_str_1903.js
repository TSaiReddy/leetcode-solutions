function largestOddNumber(num) {
  for (let i = num.length - 1; i >= 0; i--)
    if (Number(num[i]) % 2 !== 0) return num.slice(0, i + 1);
  return "";
}

console.log(largestOddNumber("52"));
console.log(largestOddNumber("4206"));
console.log(largestOddNumber("35427"));
