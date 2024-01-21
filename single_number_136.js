function singleNumber(nums) {
  const singleNum = {};
  for (const num of nums) {
    singleNum[num] = Number(singleNum[num] || 0) + 1;
  }
  for (const key in singleNum) {
    if (singleNum[key] === 1) {
      return key;
    }
  }
}

console.log(singleNumber([1]));
