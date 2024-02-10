function generate(numRows) {
  const result = [];
  for (let i = 0; i < numRows; i++) {
    const subArr = new Array(i + 1).fill(1);
    for (let j = 1; j < i; j++) {
      subArr[j] = result[i - 1][j - 1] + result[i - 1][j];
    }
    result.push(subArr);
  }
  return result;
}
console.log(generate(3));
