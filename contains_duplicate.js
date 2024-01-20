function containsDuplicate(nums) {
  const singleNum = {};
  for (const num of nums) {
    singleNum[num] = Number(singleNum[num] || 0) + 1;
  }
  for (const key in singleNum) {
    if (singleNum[key] > 1) {
      return true;
    }
  }
  return false;
}

console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]));
