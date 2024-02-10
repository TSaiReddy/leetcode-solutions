function plusOne(digits) {
  const toStr = digits.join("");
  const sum = BigInt(toStr) + BigInt(1);
  const toArr = String(sum).split("").map(Number);

  return toArr;
}

console.log(plusOne([1, 2, 3]));
console.log(plusOne([1, 2, 9]));
console.log(plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3]));
